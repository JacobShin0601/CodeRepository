#!/usr/bin/env python3

import numpy as np
import math

def dot(a, b):
	"""Compute dot product between a and b.
	Args:
		a, b: (2,) ndarray as R^2 vectors
	
	Returns:
		a number which is the dot product between a, b
	"""
	dot_product_inter_sum = 0
	for i in range(a.shape[0]):
		dot_product_inter_sum += a[i]*b[i]
		
	dot_product = dot_product_inter_sum
	
	return dot_product

# Test your code before you submit.
a = np.array([2,4])
b = np.array([3,5])
print(dot(a,b))


d = np.arccos(-1/2)
e = math.acos(-1/2)
#print(d, e)

x = np.array([1, 1, 1])
y = np.array([2, -1, 0])
A = np.array([[1, 0, 0], [0, 2, -1], [0, -1, 3]])

mul_result = np.matmul(x, A)
#print(mul_result)
mul_result = np.matmul(mul_result, y)
#mul_result = math.sqrt(mul_result)
#print(mul_result)

#mul_result2 = np.matmul(y, A)
#mul_result2 = np.matmul(mul_result2, x)
#print(mul_result2)

x_norm = np.matmul(x, A)
x_norm = np.matmul(x_norm, x)
x_norm = math.sqrt(x_norm)
y_norm = np.matmul(y, A)
y_norm = np.matmul(y_norm, y)
y_norm = math.sqrt(y_norm)
print(x_norm, y_norm)

cos_w = mul_result / (x_norm * y_norm)
print(cos_w)
w = np.arccos(cos_w)
print(w)

