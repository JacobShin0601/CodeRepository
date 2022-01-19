#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from mpl_toolkits.mplot3d import Axes3D

######################################## Data preparation #########################################

file = '/Users/Jacob_Shin/dataframe.xlsx'
df = pd.read_excel(file)

X = df[['MC Operation rate', 'PMI']].values.reshape(-1,2)
Y = df['bidding price']

######################## Prepare model data point for visualization ###############################

x = X[:, 0]
y = X[:, 1]
z = Y

x_pred = np.linspace(6, 24, 30)      # range of porosity values
y_pred = np.linspace(0.93, 2.9, 30)  # range of VR values
xx_pred, yy_pred = np.meshgrid(x_pred, y_pred)
model_viz = np.array([xx_pred.flatten(), yy_pred.flatten()]).T

################################################ Train #############################################

ols = linear_model.LinearRegression()
model = ols.fit(X, Y)
predicted = model.predict(model_viz)

############################################## Evaluate ############################################

r2 = model.score(X, Y)

############################################## Plot ################################################

plt.style.use('default')

fig = plt.figure(figsize=(12, 4))

ax1 = fig.add_subplot(131, projection='3d')
ax2 = fig.add_subplot(132, projection='3d')
ax3 = fig.add_subplot(133, projection='3d')

axes = [ax1, ax2, ax3]

for ax in axes:
	ax.plot(x, y, z, color='k', zorder=15, linestyle='none', marker='o', alpha=0.5)
	ax.scatter(xx_pred.flatten(), yy_pred.flatten(), predicted, facecolor=(0,0,0,0), s=20, edgecolor='#70b3f0')
	ax.set_xlabel('Porosity (%)', fontsize=12)
	ax.set_ylabel('VR', fontsize=12)
	ax.set_zlabel('Gas Prod. (Mcf/day)', fontsize=12)
	ax.locator_params(nbins=4, axis='x')
	ax.locator_params(nbins=5, axis='x')
	
	#ax1.text2D(0.2, 0.32, 'aegis4048.github.io', fontsize=13, ha='center', va='center',
			#transform=ax1.transAxes, color='grey', alpha=0.5)
	#ax2.text2D(0.3, 0.42, 'aegis4048.github.io', fontsize=13, ha='center', va='center',
			#transform=ax2.transAxes, color='grey', alpha=0.5)
	#ax3.text2D(0.85, 0.85, 'aegis4048.github.io', fontsize=13, ha='center', va='center',
			#transform=ax3.transAxes, color='grey', alpha=0.5)

ax1.view_init(elev=27, azim=112)
#ax2.view_init(elev=16, azim=-51)
#ax3.view_init(elev=60, azim=165)

fig.suptitle('$R^2 = %.2f$' % r2, fontsize=20)

fig.tight_layout()

plt.show()
