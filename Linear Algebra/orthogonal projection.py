#!/usr/bin/env python3

import numpy as np


# GRADED FUNCTION: DO NOT EDIT THIS LINE
def projection_matrix_1d(b):
	"""Compute the projection matrix onto the space spanned by `b`
	Args:
		b: ndarray of dimension (D,), the basis for the subspace
	
	Returns:
		P: the projection matrix
	"""
	# YOUR CODE HERE
	### Uncomment and modify the code below
	D, = b.shape
	### Edit the code below to compute a projection matrix of shape (D,D)
	P = np.zeros((D, D)) # <-- EDIT THIS
	# You may be tempted to follow the formula and implement bb^T as b @ b.T in numpy.
	# However, notice that this b is a 1D ndarray, so b.T is an no-op. Use np.outer instead
	# to implement the outer product.'
	
	B_BT = np.outer(b, b)
	norm_B = 0
	
	for i in range(D):
		norm_B += b[i]**2
		
	norm_B = np.sqrt(norm_B)
	norm_B = norm_B ** 2
	
	P = (1/norm_B) * B_BT
	
	return P 

def projection_matrix_general(B):
	"""Compute the projection matrix onto the space spanned by the columns of `B`
	Args:
		B: ndarray of dimension (D, M), the basis for the subspace
	
	Returns:
		P: the projection matrix
	"""
	# YOUR CODE HERE
	### Uncomment and modify the code below
	P = np.eye(B.shape[0]) # <-- EDIT THIS
	
	BT_B = np.transpose(B) @ B
	BT_B_inversed = np.linalg.inv(BT_B)
	P = B @ BT_B_inversed @ np.transpose(B)
	
	return P

#b = np.array([5, 3])
#print(b)
#projection_mtx = projection_matrix_1d(b)
#print(projection_mtx)

B = np.array([[5, 3], [4, 5], [7, 6]])
P = projection_matrix_general(B)
print(P)