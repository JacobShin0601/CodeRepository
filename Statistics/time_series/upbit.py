import requests
import time


days = [31,20,31,30,31,30,31,31,30,31,30,31]
def getTradePrice(market):
    url = "https://api.upbit.com/v1/candles/minutes/240"

    tot_data_cnt = 0
    check = 0
    with open('./data/2020_bitcoin_price.csv' ,'w', encoding= 'utf8') as fw:
        for i, day in enumerate(days):
            for j in range(day):
                if i < 9:
                    new_i = "0{}".format(i+1)
                else:
                    new_i = i+1  
                if j < 9:
                    new_j ="0{}".format(j+1)
                    to_j = j+2
                    if to_j < 10:
                        to_j = "0{}".format(to_j)
                else:
                    new_j = j+1
                    to_j = j+2
                    if to_j < 10:
                        to_j = "0{}".format(to_j)
                if int(to_j) > day:
                    continue
                querystring = {"market": market, "count": "6", "from":"2020-{}-{} 00:00:00".format(str(new_i), str(new_j)), "to":"2020-{}-{} 00:00:00".format(str(new_i), str(to_j))}
                print(querystring)
                response = requests.request("GET", url, params=querystring)
                check += 1
                if check == 10:
                    time.sleep(3)
                    check = 0
                for data in response.json():
                    print(data['candle_date_time_utc'])
                    tot_data_cnt+=1
                    fw.write(data['candle_date_time_utc'] + "," + str(data['trade_price']) + "\n")
    print(tot_data_cnt)
    # return response.json()[0]['trade_price']


if __name__ =='__main__':
    getTradePrice("KRW-BTC")