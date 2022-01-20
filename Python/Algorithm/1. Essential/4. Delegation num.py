#!/usr/bin/env python3

#10
#45 73 66 87 92 67 75 79 75 80

import sys
sys.stdin = open('input.txt', 'rt')

num_score = int(input())
lst_scores = list(map(int, input().split()))

sum_score = sum(lst_scores)
avg_score = int(round(sum_score / num_score, 0))
#print(avg_score)

min_score = float('inf')
min_gap = float('inf')
min_idx = float('inf')

for i in range(len(lst_scores)):
	gap = abs(lst_scores[i] - avg_score)
	
	### 1. min_gap -> 2. highest score -> 3. earlier idx
	
	### 1.5 if gaps are same among the scores
	if gap == min_gap:
		### 3. earlier idx
		if min_score == lst_scores[i]:
			next
		### 2. highest score
		elif min_score < lst_scores[i]:
			min_gap = gap
			min_score = lst_scores[i]
			min_idx = i
	### 1. min_gap
	elif gap < min_gap:
		min_gap = gap
		min_score = lst_scores[i]
		min_idx = i
		
print(str(avg_score) + " " + str(min_idx + 1))
		
	
	