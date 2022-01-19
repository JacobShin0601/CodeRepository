#!/usr/bin/env python3

import sys
sys.stdin = open('input.txt', 'rt')

input_num = int(input())
lst_sieve = [0] * (input_num + 1)
cnt = 0

for i in range(2, input_num + 1):
	if lst_sieve[i] == 0:
		cnt += 1
	
	for j in range(i, input_num + 1, i):
		lst_sieve[j] = 1
		
print(cnt)