#!/usr/bin/env python3

import numpy as np
import math

def length(x):
	"""Compute the length of a vector"""
	length_x = 0
	for i in range(len(x)):
		length_x += x[i]**2 # <--- compute the length of a vector x here.
	length_x = math.sqrt(length_x)
	return length_x

def dot_product(x, y):
	"""Compute the length of a vector"""
	dot_product_result = 0
	for i in range(len(x)):
		dot_product_result += x[i]*y[i] # <--- compute the length of a vector x here.
		#result = math.sqrt(dot_product(dot_product_intermediate)
	return dot_product_result

def rad_calculator(x, y):
	cos_result = dot_product(x, y) / ((length(x)*length(y)))
	degree = np.arccos(cos_result)
	return degree

#def rad_calculator(degree):
#	rad_result = math.radians(degree)
#	return rad_result

a = np.array([1, -1, 3])
#print(length(a))

b = np.array([3, 4])
c = np.array([-1, -1])
rad_result = rad_calculator(b, c)
print(rad_result)



d = np.array([3, 4])
e = np.array([1, -1])
#print(math.sqrt((2**2)+(5**2))) ## correct

f = np.array([1, 2, 3])
g = np.array([-1, 0, 8])

x = f
y = f-g
rad_result2 = rad_calculator(x, y)
#print(rad_result2)
#rad_result2 = rad_calculator(degree_result2)
#print(degree_result2, rad_result2)