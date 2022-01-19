#!/usr/bin/env python3

#3
#3 3 6
#2 2 2
#6 2 5


import sys
sys.stdin = open('input.txt', 'rt')

num_game = int(input())
cnt_dict = {}
lst_prize = []

for cnt_game in range(num_game):
	game_data = list(map(int, input().split()))
	
	for game_result in game_data:
		if game_result in cnt_dict:
			cnt_dict[game_result] += 1
		else:
			cnt_dict[game_result] = 1
			
	if 3 in cnt_dict.values():
		highest_key = [key for (key, value) in cnt_dict.items() if value == 3]
		highest_value = [value for (key, value) in cnt_dict.items() if value == 3]
		prize = 10000 + highest_key[0] * 1000
	elif 2 in cnt_dict.values():
		highest_key = [key for (key, value) in cnt_dict.items() if value == 2]
		highest_value = [value for (key, value) in cnt_dict.items() if value == 2]
		prize = 1000 + highest_key[0] * 100
	else:
		highest_key = max(cnt_dict.keys())
		prize = 100 * highest_key
		
	lst_prize.append(prize)
	
print(max(lst_prize))
		
		
		