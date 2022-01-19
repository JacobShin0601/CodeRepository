#!/usr/bin/env python3

#4 6
##5 6 7

import sys
sys.stdin = open('input.txt', 'rt')

n_poly, m_poly = map(int, input().split())
dict_sum = {}

for n in range(1, n_poly+1):
	for m in range(1, m_poly+1):
		if n + m not in dict_sum:
			dict_sum[n + m] = 1
		dict_sum[n + m] += 1
		
		#print(dict_sum)
#print(max(dict_sum, key=dict_sum.get))
#sorted_dict_sum = sorted(dict_sum, key = lambda x: dict_sum[x], reverse = True)
#print(sorted_dict_sum)

max_key = [key for key, value in dict_sum.items() if value == max(dict_sum.values())]
sorted_max_key = sorted(max_key)
print(sorted_max_key)

