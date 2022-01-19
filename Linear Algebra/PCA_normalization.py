#!/usr/bin/env python3

# PACKAGE: DO NOT EDIT
import numpy as np
import scipy
import scipy.stats

import matplotlib.pyplot as plt

# GRADED FUNCTION: DO NOT EDIT THIS LINE
def normalize(X):
	"""Normalize the given dataset X to have zero mean.
	Args:
		X: ndarray, dataset of shape (N,D)
	
	Returns:
		(Xbar, mean): tuple of ndarray, Xbar is the normalized dataset
		with mean 0; mean is the sample mean of the dataset.
	"""
	# YOUR CODE HERE
	### Uncomment and modify the code below
	N, D = X.shape
	
	##making mu array
	mu = np.zeros((D,)) # <-- EDIT THIS, compute the mean of X
	stdv_X = np.zeros((D,))

	
	for n in range(N):
		for d in range(D):
			mu[d] += X[n, d]
	mu = mu * (1/N)
	
#	for n in range(N):
#		for d in range(D):
#			stdv_X[d] += (X[n, d] - mu[d])**2
#	stdv_X = stdv_X * (1/N)
##	print(stdv_X)
	
	stdv_X = np.std(X)
#	print(stdv_X)

	Xbar = np.zeros((N, D))
	##normalize
	for n in range(N):
		for d in range(D):
#			print(stdv_X, X[n, d], mu[d])
			if(mu[d] == 0):
				Xbar[n, d] = X[n, d]
			else:
				Xbar[n, d] = (X[n, d] - mu[d]) / stdv_X

#	print(Xbar)
	return Xbar, mu

"""Test data normalization"""
from numpy.testing import assert_allclose


#X0 = np.array([[0, 0.0], 
#	[1.0, 1.0], 
#	[2.0, 2.0]])
##print(X0)
#X0_normalize, X0_mean = normalize(X0)
## Test that normalized data has zero mean
#assert_allclose(np.mean(X0_normalize, 0), np.zeros((2,)))
#assert_allclose(X0_mean, np.array([1.0, 1.0]))
#assert_allclose(normalize(X0_normalize)[0], X0_normalize)


X0 = np.array([[0, 0.0], 
	[1.0, 0.0], 
	[2.0, 0.0]])
#print(X0)
X0_normalize, X0_mean = normalize(X0)
# Test that normalized data has zero mean and unit variance
assert_allclose(np.mean(X0_normalize, 0), np.zeros((2,)))
assert_allclose(X0_mean, np.array([1.0, 0.0]))
assert_allclose(normalize(X0_normalize)[0], X0_normalize)

# Some hidden tests below
# ...