import requests

url = "https://api.upbit.com/v1/candles/minutes/240"
querystring = {'market': 'KRW-BTC', 'count': '6', 'from': '2020-01-11 00:00:00', 'to': '2020-01-12 00:00:00'}
response = requests.request("GET", url, params=querystring)

for data in response.json():
    print(data)