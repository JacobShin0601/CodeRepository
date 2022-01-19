with open("this_page_cache.txt", 'r') as outfile:
    outfile.write('')
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
import requests_with_caching
import json

def get_movies_from_tastedive(str_input):
    parameters = {}
    baseurl = "https://tastedive.com/api/similar"
    parameters['q'] = str_input
    parameters['type'] = "movies"
    parameters['limit'] = 5
   
    #print(resps.text)
    try:
        resps = requests_with_caching.get(baseurl, params = parameters)
        return resps.json()
    except:
        resps = {}
        return resps


def extract_movie_titles(dict_input):
    try:
        titles = []
        dict_results = dict_input['Similar']
        dict_similar = dict_results['Results']
        for item in dict_similar:
            titles.append(item['Name'])
        #print(titles)
        return titles
    
    except:
        titles = []
        return titles


def get_related_titles(lst_input):
       
    for str_input in lst_input:
        result_dict = get_movies_from_tastedive(str_input)
        result_lst = extract_movie_titles(result_dict)
    try:
        result_lst = list(set(result_lst))
        return result_lst
    except:
        result_lst = []
        return result_lst


#get_related_titles(["Black Panther", "Captain Marvel"])
#get_related_titles([])

def get_movie_data(str_input):
    try:
        baseurl = "http://www.omdbapi.com/"
        params = {'t':str_input, 'r':'json'}
        resps = requests_with_caching.get(baseurl, params = params)
        result = resps.json()
        return result
    except:
        result = {}
        return result

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages





def get_movie_rating(dict_input):
    try:
        #print(dict_input)
        rating_lst = dict_input['Ratings']
        #print(rating_lst)
        rating = 0
        for rating_dict in rating_lst:
            #print(rating_dict)
            if rating_dict['Source'] == 'Rotten Tomatoes':
                rating = rating_dict['Value']
                rating = int(rating[:-1])
        return rating            

    except:
        rating = 0
        return rating