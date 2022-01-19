import requests
import json
import requests_with_caching

d = {'q': '"violins and guitars"', 'tbm': 'isch'}
results = requests.get("https://google.com/search", params=d)
print(results.url)

results2 = requests_with_caching.get("https://google.com/search", params=d)
print(results2.url)