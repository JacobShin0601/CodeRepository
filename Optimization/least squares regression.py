#!/usr/bin/env python3

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

N = np.arange(2, 10000, step=10)
# Your code comes here, which calculates \hat{\theta} for different dataset sizes.

theta_error = np.zeros(N.shape)

theta_error = np.ones(N.shape) # <-- EDIT THIS
print(theta_error.shape)
print(theta_error[0])

for i in range(N[0]):
	x = np.linspace(0, 10, num=1000)
	theta = 2
	theta_hat = 2
	random = np.random.RandomState(42)
	theta_hat = theta * x
	theta = theta * x + random.normal(scale=1.0, size=len(x))
	
	norm_theta = np.sqrt((theta_hat-theta)**2)
	
	theta_error = norm_theta
	
	
plt.plot(theta_error)
plt.xlabel("dataset size")
plt.ylabel("parameter error"); 
plt.show()