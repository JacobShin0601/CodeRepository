#!/usr/bin/env python3

#5
#level
#moon
#abcba
#soon
#gooG

import sys
sys.stdin = open('input.txt', 'rt')
num_words = int(input())

lst_words = []
while(True):
	try:
		word = str(input().strip()).lower()
		lst_words.append(word)
	except:
		break
	
	#print(lst_words)

word_seq = 1
for word in lst_words:
	retro_cnt = len(word)
	reversed_word = ''
	
	for i in range(len(word)):
		reversed_word += word[len(word)-1-i]
	
	if reversed_word == word:
		print('#'+str(word_seq)+' '+'YES')
		word_seq += 1
	else:
		print('#'+str(word_seq)+' '+'No')
		word_seq += 1
		