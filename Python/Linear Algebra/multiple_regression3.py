#!/usr/bin/env python3

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression



df=pd.read_excel('dataframe.xlsx')

#df에서 Horsepower, MPG.city 열의 값을 불러와서 배열로 짝지음
X = df[['MC Operation rate', 'PMI']].values.reshape(-1,2)  
Y = df['bidding price']

# 시각화를 위한 데이터 준비

x = X[:, 0] #Horsepower 열 값만 array로 가져옴
y = X[:, 1] #MPG.city 열 값만 array로 가져옴
z = Y

#각 독립변수들의 range 지정: 데이터 중 최소값, 최대값, 그 구간을 10으로 설정
x_pred = np.linspace(df['MC Operation rate'].min(), df['MC Operation rate'].max(), 10)
y_pred = np.linspace(df['PMI'].min(), df['PMI'].max(), 10)
xx_pred, yy_pred = np.meshgrid(x_pred, y_pred)
model_viz = np.array([xx_pred.flatten(), yy_pred.flatten()]).T

#sklearn의 linear_model.LinearRegression()함수로 다중선형회귀식을 만들고,
ols = LinearRegression()
model = ols.fit(X, Y)

#위에서 만든 model_viz 값을 넣어 다중선형회귀식의 예측값을 얻음
predicted = model.predict(model_viz)

# 해당 다중선형회귀식의 결정계수 R^2을 구함: 회귀식의 실제 데이터에 대한 설명력을 확인

r2 = model.score(X, Y)

#다중선형회귀 그래프 그리기

plt.style.use('default')

fig = plt.figure(figsize=(12, 4))

ax1 = fig.add_subplot(131, projection='3d')
ax2 = fig.add_subplot(132, projection='3d')
ax3 = fig.add_subplot(133, projection='3d')

axes = [ax1, ax2, ax3]

for ax in axes:
	ax.plot(x, y, z, color='#521FD1', zorder=100, linestyle='none', marker='o', alpha=0.2) #검은색 마커들
	ax.scatter(xx_pred.flatten(), yy_pred.flatten(), predicted, s=30, edgecolor='#70b3f0') #파란색 마커들
	ax.set_xlabel('MC Operation rate', fontsize=9) #해당 축을 설명하는 라벨
	ax.set_ylabel('PMI', fontsize=9)
	ax.set_zlabel('Bidding Price', fontsize=9)
	ax.locator_params(nbins=6, axis='x') #해당 축의 구간 개수 (쪼개진 구간도 포함)
	ax.locator_params(nbins=4, axis='y')
	ax.locator_params(nbins=4, axis='z')
	
#높이와 방위각을 조절해서 보고 싶은 위치를 조정할 수 있음
#elevation (높이), azimuth (방위각)
ax1.view_init(elev=27, azim=112) 
ax2.view_init(elev=4, azim=114)
ax3.view_init(elev=60, azim=165)

#fig.suptitle('$R^2 = %.2f$' % r2, fontsize=20)

fig.tight_layout()
plt.show()