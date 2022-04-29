#!/usr/bin/env python3

def only_alpha_numeric_characters(string):
	alpha_numeric_string = (''.join(filter(str.isalnum, string))).lower()
	return alpha_numeric_string
	
def size_of_string(string):
	size = len(string)
	return size

def palindrome_checker(string):
	match_tag = True
	cnt = 0
	
	alpha_numeric_string = only_alpha_numeric_characters(string)
	size = size_of_string(alpha_numeric_string)
	
	while(cnt != size):
		if(alpha_numeric_string[cnt] != alpha_numeric_string[size-cnt-1]):
			match_tag = False
			break;
		cnt = cnt + 1
	
	return match_tag

	#return multi_tagging ## is on the parameter
		
def result_printer(tag):
	if(tag == True):
		print("Your sentence is a palindrome")
	else:
		print("You sentence is not a palindrome")
	
def main():
	input_string = input("Please enter a sentence: ")
	
	result_tag = palindrome_checker(input_string
	)
	result_printer(result_tag)
	
main()
#Was it a car or a cat I saw?
	
	


#print(size_of_trimmed_string)
#print(alpha_numeric_string)