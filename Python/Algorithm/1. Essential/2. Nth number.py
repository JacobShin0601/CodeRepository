#!/usr/bin/env python3

import sys
sys.stdin = open('input.txt', 'rt')

def nth_number():
	parameter = list(input().split())
	cnt_num, start_num, end_num, nth_num = parameter[0], parameter[1], parameter[2], parameter[3]
	
	start_num = int(start_num) - 1
	end_num = int(end_num)
	nth_num = int(nth_num) - 1
	
	input_num = list(input().split())
	int_num = list(map(int, input_num))
	filtered_num = int_num[start_num : end_num]
	sorted_num = sorted(filtered_num)

	target_num = sorted_num[nth_num]
	return target_num



case_number = int(input())
print("Case: "+str(case_number))

cnt = 1

while(True):
	if cnt != case_number+1:
		try:
			target = nth_number()
			print("#"+str(cnt)+" "+str(target))
			cnt += 1
		except:
			print("EOF")
			break
	else:
		break

	
	