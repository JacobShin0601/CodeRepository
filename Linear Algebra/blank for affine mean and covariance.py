#!/usr/bin/env python3

import numpy as np

def affine_mean(mean, A, b):
	"""Compute the mean after affine transformation
	Args:
		mean: `ndarray` of shape (D,), the sample mean vector for some dataset.
		A, b: `ndarray` of shape (D, D) and (D,), affine transformation applied to x
	Returns:
		sample mean vector of shape (D,) after affine transformation.
	"""
	# YOUR CODE HERE
	### Uncomment and edit the code below
#     ### Edit the code below to compute the mean vector after affine transformation
	affine_m = np.zeros(mean.shape) # affine_m has shape (D,)
	### Update affine_m
	for m in range(mean.shape[0]):
		for a in range(A.shape[1]):
			#affine_m[1,] += A[1, 1]*m[1, ]
			#     += A[1, 2]*m[2, ]
			affine_m[m, ] += A[m, a]*mean[a, ]
		affine_m[m, ] += b[m]
			###
	return affine_m

# GRADED FUNCTION: DO NOT EDIT THIS LINE
def affine_covariance(S, A, b):
	"""Compute the covariance matrix after affine transformation
	
	Args:
		mean: `ndarray` of shape (D,), the sample covariance matrix for some dataset.
		A, b: `ndarray` of shape (D, D) and (D,), affine transformation applied to x
	
	Returns:
		sample covariance matrix of shape (D, D) after the transformation
	"""
	# YOUR CODE HERE
	### Uncomment and edit the code below
	### EDIT the code below to compute the covariance matrix after affine transformation

	affine_cov = np.zeros((S.shape[0], S.shape[0])) # affine_cov has shape (D, D)

	### Update affine_cov
#	for n in range(S.shape[0]):
#		for d in range(S.shape[0]):
#			for a in range(S.shape[0]):
#				affine_cov[n, d] += 
#				for c in range(S.shape[0]):
#					affine_cov[n, d] += A[a, c] * S[c, a]
	AS = np.matmul(A, S)
	AT = np.transpose(A)
	affine_cov = np.matmul(AS, AT)
	###
	return affine_cov

A = np.array([[0, 1], [2, 3]])
b = np.ones(2)
m = np.full((2, ), 2)
S = np.eye(2)*2

print(A, b, m, S)
print('\n')


affined_m = affine_covariance(S, A, b)
print(affined_m)



#expected_affine_mean = np.array([ 3., 11.])
#expected_affine_cov = np.array(
#	[[ 2.,  6.],
#	[ 6., 26.]])