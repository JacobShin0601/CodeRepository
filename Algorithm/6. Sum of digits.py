#!/usr/bin/env python3

import sys
sys.stdin = open('input.txt', 'rt')

def digit_sum(int_input):
	digit_sum = 0
	while(True):
		if(int_input>=10):
			digit_sum += int_input%10
			int_input = int(int_input/10)
		elif(int_input>=0):
			digit_sum += int_input
			break
	return digit_sum
		

num_input = map(int, input())
numbers = list(map(int, input().split()))
max_sum = float('-inf')
max_num = 0

for number in numbers:
	temp_sum = digit_sum(number)
	if temp_sum > max_sum:
		max_sum = temp_sum
		max_num = number
		
		#print(max_sum)
print(max_num)
	


			