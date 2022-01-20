#!/usr/bin/env python3

lst = [5, 3, 7, 9, 2, 5, 2, 6]

min = float('inf')

for i in lst:
	if i < min:
		min = i


print(min)