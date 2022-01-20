#!/usr/bin/env python3

#10
#1 0 1 1 1 0 0 1 1 0

import sys
sys.stdin = open('input.txt', 'rt')

cnt_input = int(input())
lst_score = list(map(int, input().split()))
lst_final_score = []
consecutive_score = 0

for i in range(len(lst_score)):

	if lst_score[i] == 0:
		lst_final_score.append(0)
		consecutive_score = 0
	else:
		lst_final_score.append(consecutive_score+1)
		consecutive_score += 1
		
print(sum(lst_final_score))
		
