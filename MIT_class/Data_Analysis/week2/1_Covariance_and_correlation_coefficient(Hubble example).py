import numpy as np

Xs = np.array([0.0339, 0.0423, 0.213, 0.257, 0.273, 0.273, 0.450, 0.503, 0.503, \
0.637, 0.805, 0.904, 0.904, 0.910, 0.910, 1.02, 1.11, 1.11, 1.41, \
1.72, 2.03, 2.02, 2.02, 2.02])

Ys = np.array([-19.3, 30.4, 38.7, 5.52, -33.1, -77.3, 398.0, 406.0, 436.0, 320.0, 373.0, \
93.9, 210.0, 423.0, 594.0, 829.0, 718.0, 561.0, 608.0, 1.04E3, 1.10E3, \
840.0, 801.0, 519.0])

N = 24

Xmean = Xs.sum()/N 
Ymean = Ys.sum()/N 
print(np.average(Xs))
print(np.average(Ys))

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

slope_beta1 = Y_stdev/X_stdev*XY_corr_coeff
print(slope_beta1)
##beta1 = XYr * (Ystd/Xstd)

intercept_beta0 = Ymean - Xmean*slope_beta1
print(intercept_beta0)
# Ymean - beta1 * Xmean



### Phase 2
Xs = np.array([ 0.387, 0.723, 1.00, 1.52, 5.20, 9.54, 19.2, 30.1, 39.5 ])
##semi-major axis of each planet's orbit
Ys = np.array([ 0.241, 0.615, 1.00, 1.88, 11.9, 29.5, 84.0, 165.0, 248 ])
## orbital period of the planet
N = 9

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