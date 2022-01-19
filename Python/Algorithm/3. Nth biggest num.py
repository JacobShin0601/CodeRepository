#!/usr/bin/env python3

#10 3
#13 15 34 23 45 65 33 11 26 42
#[65, 45, 42, 34, 33, 26, 23, 15, 13, 11]

import sys
sys.stdin = open('input.txt', 'rt')

num_card, nth_card = map(int, input().split())
cards = list(map(int, input().split()))
sorted_cards = sorted(cards, reverse = True)
#print(sorted_cards)

set_sum = set()

a, b, c = 1, 2, 3

for i in range(num_card):
	for j in range(i+1, num_card):
		for m in range(j+1, num_card):
			set_sum.add(sorted_cards[i] + sorted_cards[j] + sorted_cards[m])
			#print(sorted_cards[i])
			#print(sorted_cards[j])
			#print(sorted_cards[m])
			#print("-----")
			
lst_sum = sorted(list(set_sum), reverse = True)
print(lst_sum[nth_card-1])