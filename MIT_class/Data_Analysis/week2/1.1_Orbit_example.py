##import matplotlib.pyplot
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
#import statsmodels.formula.api as smf


### Phase 2
Xs = np.array([ 0.387, 0.723, 1.00, 1.52, 5.20, 9.54, 19.2, 30.1, 39.5 ])
##semi-major axis of each planet's orbit
Ys = np.array([ 0.241, 0.615, 1.00, 1.88, 11.9, 29.5, 84.0, 165.0, 248 ])
## orbital period of the planet
N = 9

Xmean = Xs.sum()/N 
Ymean = Ys.sum()/N 

##Xstd = np.sqrt(np.sum((Xs-Xmean)**2)/(N-1))
##Ystd = np.sqrt(np.sum((Ys-Ymean)**2)/(N-1))
X_stdev = np.std(Xs, ddof=1)
Y_stdev = np.std(Ys, ddof=1)
print(X_stdev, Y_stdev)

sum = 0
for i in range(Xs.size):
    sum += (Xs.item(i)-Xmean)*(Ys.item(i)-Ymean)

covariance_X_Y = sum/(N-1)
print(covariance_X_Y)
##XYcov = np.sum((Xs-Xmean)*(Ys-Ymean))/(N-1)

XY_corr_coeff = np.sum((Xs-Xmean)/X_stdev*(Ys-Ymean)/Y_stdev)/(N-1)
print(XY_corr_coeff)
##XYr = XYcov/(Xstd*Ystd)


sm.qqplot(Xs, line='s')
plt.title("X distribution")
##plt.show()

log_Xs = np.log10(Xs)
log_Ys = np.log10(Ys)
print(log_Xs, log_Ys)

model = sm.OLS(Ys,Xs)
results = model.fit()
