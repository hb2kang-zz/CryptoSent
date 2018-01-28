# importing the requests library
import requests

import http.client as httplib
import urllib
import json

# for crypto data
from datetime import datetime
from time import mktime

from newsapi import NewsApiClient

# Get Request
# def crypto_news(mode, coin, date, apiKey = "00f61addc87f43299865eca28c4990fa"):
#     # api-endpoint
#     URL = "https://newsapi.org/v2/" + mode
#     #sources for crypto newsapi
#
#     # defining a params dict for the parameters to be sent to the API
#     PARAMS = {'q':coin, 'from': date, 'sortBy':'popularity','apiKey': apiKey}
#     # sending get request and saving the response as response object
#     r = requests.get(url = URL, params = PARAMS)
#
#     # extracting data in json format
#     data = r.json()['articles']
#
#     return data

def crypto_news(coin, start, final):

    newsapi = NewsApiClient(api_key="00f61addc87f43299865eca28c4990fa")

    all_articles = newsapi.get_everything(q=coin,
                                      from_parameter=start,
                                      to=final,
                                      language='en',
                                      sort_by='relevancy')
    data = all_articles['articles']

    description_list = []

    for i in data:
        description_list.append(i["description"])

    return data, description_list

def bing_news(search_term):

    subscription_key = '876a5eaf8f574cf1856c201c18f20997'
    search_url = 'https://api.cognitive.microsoft.com/bing/v7.0/news/search'

    headers = {"Ocp-Apim-Subscription-Key" : subscription_key}

    params  = {"q": search_term, "textDecorations": True, "textFormat": "HTML", "sortBy": "Date", "since": 946684800}
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

    # All the value
    value = search_results["value"]

    # descriptions = [article["description"] for article in search_results["value"]]

    return value

# Post individual sentiment from azure
def GetSentiment(text):

    "Gets the sentiments for a set of documents and returns the information."

    accessKey ="c1029950d5e14c72808339af683178ef"

    uri = 'eastus.api.cognitive.microsoft.com'

    path = '/text/analytics/v2.0/sentiment'

    headers = {'Ocp-Apim-Subscription-Key': accessKey}
    conn = httplib.HTTPSConnection(uri)

    documents = { 'documents': [
    { 'id': '1', 'language': 'en', 'text': text},
    ]}

    body = json.dumps(documents)
    conn.request("POST", path, body, headers)
    response = conn.getresponse()

    result = response.read().decode('utf-8')

    json_result = json.loads(result)
    print(json_result)

    try:
        score = json_result['documents'][0]["score"]
    except Exception:
        score = 0

    return score

# function to create list of strings
# strings of description
def description(data):

    data_list = []
    for i in range(len(data)):
        data_list.append(data[i]["description"])

    return data_list

# Crypto historical data
def crypto_data(coin, start, end, period):
    # api-endpoint
    # URL = "https://poloniex.com/public?command=returnOrderBook&currencyPair=BTC_NXT&depth=10"
    #sources for crypto newsapi
    URL = "https://poloniex.com/public?"

    start_unix = mktime(datetime.strptime(start, "%Y-%m-%d").timetuple())
    end_unix = mktime(datetime.strptime(end, "%Y-%m-%d").timetuple())

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'command':"returnChartData", 'currencyPair': coin, 'start': start_unix, 'end': end_unix, 'period': period}
    # sending get request and saving the response as response object
    r = requests.get(url = URL, params = PARAMS)

    # extracting data in json format
    data = r.json()

    return data

# Creates news, sent dictionary
def sent_dict(description, description_list, descending = True):

    sentiments = dict()

    for i in description:
        sentiments[i["description"]] = GetSentiment(i["description"])

    score_list = []

    for keys, value in sentiments.items():
        score_list.append(value)

    # sorted score list descending
    sorted_score = sorted(score_list, reverse = descending)
    # create dictionary object
    sorted_dict = dict()

    sorted_description = []

    for i in sorted_score:
        for key, value in sentiments.items():    # for name, age in list.items():  (for Python 3.x)
            if value == i:
                sorted_dict[key] = i
                sorted_description.append(key)

    # Returns an ordered dictionary from descending order of scores with a key as the description and the score as the value
    return sorted_dict, sorted_score, sorted_description

def score(data):
    # returns a list of strings

    list_score = []

    for i in data:
        list_score.append(str(GetSentiment(i["description"])))

    return list_score

def coin_to_json(coin_data):

    x = []
    y = []

    for i in coin_data:
        t = datetime.fromtimestamp(i['date'])

        x.append(t.strftime('%Y-%m-%d'))
        y.append(i["close"])

    plot_data = []

    for i in range(len(x)):
        plot_data.append({'x': x[i], 'y': y[i]})

    return json.dumps(plot_data)

def changes_bitcoin():

    url = 'https://api.coinmarketcap.com/v1/ticker/'
    headers = {'limit' : '10'}
    response = requests.get(url, headers=headers)

    response.raise_for_status()
    results = response.json()

    percent_change_7d = results[0]["percent_change_7d"]
    percent_change_1h = results[0]["percent_change_1h"]
    percent_change_24h = results[0]['percent_change_24h']

    return percent_change_1h, percent_change_24h, percent_change_7d

def changes_ethereum():

    url = 'https://api.coinmarketcap.com/v1/ticker/'
    headers = {'limit' : '10'}
    response = requests.get(url, headers=headers)

    response.raise_for_status()
    results = response.json()

    percent_change_7d = results[1]["percent_change_7d"]
    percent_change_1h = results[1]["percent_change_1h"]
    percent_change_24h = results[1]['percent_change_24h']

    return percent_change_1h, percent_change_24h, percent_change_7d

def changes_ripple():

    url = 'https://api.coinmarketcap.com/v1/ticker/'
    headers = {'limit' : '10'}
    response = requests.get(url, headers=headers)

    response.raise_for_status()
    results = response.json()

    percent_change_7d = results[2]["percent_change_7d"]
    percent_change_1h = results[2]["percent_change_1h"]
    percent_change_24h = results[2]['percent_change_24h']

    return percent_change_1h, percent_change_24h, percent_change_7d

def changes_BTC_cash():

    url = 'https://api.coinmarketcap.com/v1/ticker/'
    headers = {'limit' : '10'}
    response = requests.get(url, headers=headers)

    response.raise_for_status()
    results = response.json()

    percent_change_7d = results[3]["percent_change_7d"]
    percent_change_1h = results[3]["percent_change_1h"]
    percent_change_24h = results[3]['percent_change_24h']

    return percent_change_1h, percent_change_24h, percent_change_7d

def changes_LTC():

    url = 'https://api.coinmarketcap.com/v1/ticker/'
    headers = {'limit' : '10'}
    response = requests.get(url, headers=headers)

    response.raise_for_status()
    results = response.json()

    percent_change_7d = results[6]["percent_change_7d"]
    percent_change_1h = results[6]["percent_change_1h"]
    percent_change_24h = results[6]['percent_change_24h']

    return percent_change_1h, percent_change_24h, percent_change_7d

def changes_Stellar():

    url = 'https://api.coinmarketcap.com/v1/ticker/'
    headers = {'limit' : '10'}
    response = requests.get(url, headers=headers)

    response.raise_for_status()
    results = response.json()

    percent_change_7d = results[5]["percent_change_7d"]
    percent_change_1h = results[5]["percent_change_1h"]
    percent_change_24h = results[5]['percent_change_24h']

    return percent_change_1h, percent_change_24h, percent_change_7d
