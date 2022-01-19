#!/usr/bin/env python3

import sys
sys.stdin = open('input.txt', 'rt')

n, k = map(int, input().split())

lst_divisor = []

for i in range(1, n+1):
	if n % i == 0:
		lst_divisor.append(i)
	
try:	
	print(lst_divisor[k-1])
	print(lst_divisor)
except:
	print(-1)