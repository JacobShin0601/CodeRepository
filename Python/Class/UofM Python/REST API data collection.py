#!/usr/bin/env python3


# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movies_from_tastedive("Bridesmaids")
# get_movies_from_tastedive("Black Panther")

import requests
import json

def get_movies_from_tastedive(str_input):
	baseurl = "https://tastedive.com/api/similar"
	parameters = {'q':str_input, 'type':'movies', 'limit':5}
	resps = requests.get(baseurl, params = parameters)
	five_result = resps.json()
	#print(five_result)
	
	similar_titles = []
	results_lst = five_result['Similar']['Results']
	#print(results_lst)
	for i in range(len(results_lst)):
		title_dict = results_lst[i]
		title = title_dict['Name']
		#print(title)
		similar_titles.append(title)
	similar_titles_dict = {'Similar':similar_titles}
	return similar_titles_dict

print(get_movies_from_tastedive("Bridesmaids"))
print(get_movies_from_tastedive("Black Panther"))
