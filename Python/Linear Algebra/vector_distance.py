#!/usr/bin/env python3

import numpy as np
# GRADED FUNCTION: DO NOT EDIT THIS LINE

def distance(x0, x1):
	"""Compute distance between two vectors x0, x1 using the dot product.
	
	Args:
	x0, x1: ndarray of shape (D,) to compute distance between. 
	
	Returns:
	the distance between the x0 and x1.
	"""
	# YOUR CODE HERE
	## Uncomment and modify the code below
	vector_distance = x0 - x1
#	print(np.shape(vector_distance))
#	len_vector = int(vector_distance[0]) + 1
#	print(len_vector)
	distance_sum = 0
#	print(np.shape(vector_distance))
	
	for i in range(np.shape(vector_distance)[0]):
		distance_sum += ((vector_distance[i])**2)
		
	distance = np.sqrt(distance_sum) # <-- EDIT THIS to compute the distance between x0 and x1
	return distance

# Some sanity checks, you may want to have more interesting test cases to test your implementation
a = np.array([1, 0])
b = np.array([0, 1])
np.testing.assert_allclose(distance(a, b), np.sqrt(2), rtol=1e-7)

a = np.array([1, 0])
b = np.array([1., np.sqrt(3)])
np.testing.assert_allclose(distance(a, b), np.sqrt(3), rtol=1e-7)