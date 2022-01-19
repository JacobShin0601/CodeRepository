#!/usr/bin/env python3



def remainingwords(string):
	segmented_string = string.split()
	concatenated_words = ''
	for i in range(1, len(segmented_string)):
		concatenated_words += segmented_string[i]
		concatenated_words += ' '
		
	concatenated_words = concatenated_words.strip()
	return concatenated_words


#sample_string = "the quick brown box"
#print(remainingwords(sample_string))