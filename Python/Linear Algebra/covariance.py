#!/usr/bin/env python3

import numpy as np

def mean_naive(X):
	"""Compute the sample mean for a dataset by iterating over the dataset.
	
	Args:
		X: `ndarray` of shape (N, D) representing the dataset. N 
		is the size of the dataset and D is the dimensionality of the dataset.
	Returns:
		mean: `ndarray` of shape (D, ), the sample mean of the dataset `X`.
	"""
	# YOUR CODE HERE
	### Uncomment and edit the code below
	#iterate over the dataset and compute the mean vector.
	N, D = X.shape
	mean = np.zeros((D,))
	for n in range(N):
		for count_D in range(D):
			mean[count_D] += X[n, count_D]
		mean_D = mean/N
	return mean_D

def cov_naive(X):
	"""Compute the sample covariance for a dataset by iterating over the dataset.
	
	Args:
		X: `ndarray` of shape (N, D) representing the dataset. N 
		is the size of the dataset and D is the dimensionality of the dataset.
	Returns:
		ndarray: ndarray with shape (D, D), the sample covariance of the dataset `X`.
	"""
	# YOUR CODE HERE
	### Uncomment and edit the code below
	N, D = X.shape
	### Edit the code below to compute the covariance matrix by iterating over the dataset.
	covariance = np.zeros((D, D))
	mean_matrix = mean_naive(X)
	### Update covariance
	for n in range(D):
		for d in range(D):
			for a in range(N):
				covariance[n, d] += ((X[a, n] - mean_matrix[n]) * (X[a, d] - mean_matrix[d]))
			# for example [0, 1] -> XY calculation
			# (x[a, 0] - x_mean) * ( x[a, 1] - y_mean)
			
		##     X    Y    Z
		## X  XX   XY    XZ
		## Y  YX   YY    YZ
		## Z  ZX   ZY    ZZ
		
	covariance = covariance/N
	###
	return covariance


D = np.array([[64, 580, 29], [66, 570, 33], [68, 590, 37], [69, 660, 46], [73, 600, 55]])
print(D)
print('\n')

mean_D = mean_naive(D)
print(mean_D)
print('\n')

cov_D = cov_naive(D)
print(cov_D)
print('\n')

m = np.zeros((D.shape[1]))
print(m)




#cov_D = np.cov(D)
#print(cov_D)

