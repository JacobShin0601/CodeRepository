#!/usr/bin/env python3

import sys
sys.stdin = open('input.txt', 'rt')

def isPrimeNumber(int_input): 
	flag_prime = True
	for i in range(2, int_input):
		if int_input % i == 0:
			flag_prime = False
			break
	return flag_prime
#7300
def reversed_number(int_input):
	str_input = str(int_input)
	reversed_num = ''
	for i in range(len(str_input)-1, -1, -1):
		reversed_num += str_input[i]
	reversed_num = int(reversed_num)
	return reversed_num

num_cnt = int(input())
lst_num = list(map(int, input().split()))

for number in lst_num:
	reversed_num = reversed_number(number)
	if isPrimeNumber(reversed_num) == True:
		print(reversed_num)
	
	