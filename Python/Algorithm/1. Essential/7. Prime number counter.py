#!/usr/bin/env python3

import sys
sys.stdin = open('input.txt', 'rt')


def isPrimeNumber(int_input): 
	flag_prime = True
	for i in range(2, int_input):
		if int_input%i == 0:
			flag_prime = False
			break
	return flag_prime


input_num = int(input())
cnt = 1

for x in range(3, input_num+1):
	if isPrimeNumber(x) == True:
		cnt += 1
print(cnt)