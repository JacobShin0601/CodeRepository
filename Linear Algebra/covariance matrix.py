#!/usr/bin/env python3

import numpy as np

# GRADED FUNCTION: DO NOT EDIT THIS LINE
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
	covariance = covariance/N
	
	return covariance


def mean(X):
	"""Compute the sample mean for a dataset.
	
	Args:
		X: `ndarray` of shape (N, D) representing the dataset. N 
		is the size of the dataset and D is the dimensionality of the dataset.
	Returns:
		ndarray: ndarray with shape (D,), the sample mean of the dataset `X`.
	"""
	# YOUR CODE HERE
	### Uncomment and edit the code below
	N, D = X.shape
	m = np.zeros((X.shape[1]))
	
	for n in range(N):
		for d in range(D):
			m[d] += X[n, d]
	m = m/X.shape[0]
	return m

def cov(X):
	"""Compute the sample covariance for a dataset.
	
	Args:
		X: `ndarray` of shape (N, D) representing the dataset. N 
		is the size of the dataset and D is the dimensionality of the dataset.
	Returns:
		ndarray: ndarray with shape (D, D), the sample covariance of the dataset `X`.
	"""
	# YOUR CODE HERE
	
	# It is possible to vectorize our code for computing the covariance with matrix multiplications,
	# i.e., we do not need to explicitly
	# iterate over the entire dataset as looping in Python tends to be slow
	# We challenge you to give a vectorized implementation without using np.cov, but if you choose to use np.cov,
	# be sure to pass in bias=True.
	### Uncomment and edit the code below
	N, D = X.shape
	### Edit the code to compute the covariance matrix
	covariance_matrix = np.zeros((D, D))
	### Update covariance_matrix here
	mean_matrix = mean(X)
	### Update covariance
	for n in range(D):
		for d in range(D):
			for a in range(N):
				covariance[n, d] += ((X[a, n] - mean_matrix[n]) * (X[a, d] - mean_matrix[d]))
				
	covariance_matrix = covariance/N
	
	###
	return covariance_matrix


from numpy.testing import assert_allclose

# Test case 1
X = np.array([[0., 1., 1.], 
			  [1., 2., 1.]])
expected_mean = np.array([0.5, 1.5, 1.])
assert_allclose(mean(X), expected_mean, rtol=1e-5)

# Test case 2
X = np.array([[0., 1., 0.], 
							[2., 3., 1.]])
expected_mean = np.array([1., 2., 0.5])
assert_allclose(mean(X), expected_mean, rtol=1e-5)

# Test covariance is zero
X = np.array([[0., 1.], 
							[0., 1.]])
expected_mean = np.array([0., 1.])
assert_allclose(mean(X), expected_mean, rtol=1e-5)

### Some hidden tests below
### ...