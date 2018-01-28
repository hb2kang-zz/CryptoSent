from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView


from api import *


# class indexView(TemplateView):
#
#     template_name = "crypto/index.html"
#
#     def get(self, request):


# Create your views here.
def index(request):

    # value = bing_news("Bitcoin")
    #
    # #indivudual score value
    # # sent = GetSentiment(value[1]["description"])["documents"][0]["score"]
    #
    # sent = GetSentiment(cryp_news[0]["description"])
    #
    #
    # context = {
    #     'title': 'title and description',
    #     'sentiment': score_list,
    #     'news': cryp_news,
    #     'value': value,
    #
    # }

    return render(request, 'crypto/index.html')

def display(request):
    return render(request, 'crypto/display.html')

def bitcoin(request):

    # Crypto news from specific news api
    # parameters
    # coin or search parameter
    # start
    # end
    cryp_news, description_list = crypto_news("Bitcoin", "2017-09-01", "2018-01-30")

    # sentiment list
    cryp_news_dict, score_list, sorted_description = sent_dict(cryp_news, description_list, descending = False)

    score_ = score(cryp_news)

    # # Bing NEWS
    # bing = bing_news("Bitcoin")

    # coin_data = crypto_data('USDT_BTC', "2018-01-01","2018-01-27", 14400)
    #
    # coin_json = coin_to_json(coin_data)

    percent_change_1h, percent_change_24h, percent_change_7d = changes_bitcoin()

    context = {
        'title': 'Data',
        'news': cryp_news,
        'sentiment': score_list,
        'score': score_,
        'change_1': percent_change_1h,
        'change_24': percent_change_24h,
        'change_7': percent_change_7d
    }

    return render(request, 'crypto/bitcoin.html', context)

#{'json_data': json.dumps({'a':10, 'b':11, 'c':12})

def ethereum(request):

    # Crypto news from specific news api
    # parameters
    # coin or search parameter
    # start
    # end
    cryp_news, description_list = crypto_news("Ethereum Cryptocurrency", "2017-09-01", "2018-01-30")

    # sentiment list
    cryp_news_dict, score_list, sorted_description = sent_dict(cryp_news, description_list, descending = False)

    score_ = score(cryp_news)

    # # Bing NEWS
    # bing = bing_news("Ethereum")

    # coin_data = crypto_data('USDT_ETH', "2018-01-01","2018-01-27", 14400)
    #
    # coin_json = coin_to_json(coin_data)

    percent_change_1h, percent_change_24h, percent_change_7d = changes_ethereum()

    context = {
        'title': 'Data',
        'news': cryp_news,
        'sentiment': score_list,
        'score': score_,
        'change_1': percent_change_1h,
        'change_24': percent_change_24h,
        'change_7': percent_change_7d
    }

    return render(request, 'crypto/ethereum.html', context)

def litecoin(request):

    # Crypto news from specific news api
    # parameters
    # coin or search parameter
    # start
    # end
    cryp_news, description_list = crypto_news("LiteCoin", "2017-09-01", "2018-01-30")

    # sentiment list
    cryp_news_dict, score_list, sorted_description = sent_dict(cryp_news, description_list, descending = False)

    score_ = score(cryp_news)

    # # Bing NEWS
    # bing = bing_news("Ethereum")

    # coin_data = crypto_data('USDT_LTC', "2018-01-01","2018-01-27", 14400)
    #
    # coin_json = coin_to_json(coin_data)

    percent_change_1h, percent_change_24h, percent_change_7d = changes_LTC()

    context = {
        'title': 'Data',
        'news': cryp_news,
        'sentiment': score_list,
        'score': score_,
        'change_1': percent_change_1h,
        'change_24': percent_change_24h,
        'change_7': percent_change_7d
    }
    return render(request, 'crypto/litecoin.html', context)

def ripple(request):

    # Crypto news from specific news api
    # parameters
    # coin or search parameter
    # start
    # end
    cryp_news, description_list = crypto_news("Ripple Cryptocurrency", "2017-09-01", "2018-01-30")

    # sentiment list
    cryp_news_dict, score_list, sorted_description = sent_dict(cryp_news, description_list, descending = False)

    score_ = score(cryp_news)

    # coin_data = crypto_data('USDT_XRP', "2018-01-01","2018-01-27", 14400)
    #
    # coin_json = coin_to_json(coin_data)

    percent_change_1h, percent_change_24h, percent_change_7d = changes_ripple()

    context = {
        'title': 'Data',
        'news': cryp_news,
        'sentiment': score_list,
        'score': score_,
        'change_1': percent_change_1h,
        'change_24': percent_change_24h,
        'change_7': percent_change_7d
    }
    return render(request, 'crypto/ripple.html', context)

def bitcoincash(request):

    # Crypto news from specific news api
    # parameters
    # coin or search parameter
    # start
    # end
    cryp_news, description_list = crypto_news("Bitcoin Cash", "2017-09-01", "2018-01-30")

    # sentiment list
    cryp_news_dict, score_list, sorted_description = sent_dict(cryp_news, description_list, descending = False)

    score_ = score(cryp_news)

    # Bing NEWS
    # bing = bing_news("Bitcoin Cash")

    # coin_data = crypto_data('USDT_BCH', "2018-01-01","2018-01-27", 14400)
    #
    # coin_json = (coin_to_json(coin_data))

    percent_change_1h, percent_change_24h, percent_change_7d = changes_BTC_cash()

    context = {
        'title': 'Data',
        'news': cryp_news,
        'sentiment': score_list,
        'score': score_,
        'change_1': percent_change_1h,
        'change_24': percent_change_24h,
        'change_7': percent_change_7d
    }

    return render(request, 'crypto/bitcoincash.html', context)

def stellar(request):

    # Crypto news from specific news api
    # parameters
    # coin or search parameter
    # start
    # end
    cryp_news, description_list = crypto_news("Stellar Cryptocurrency", "2017-09-01", "2018-01-30")

    # sentiment list
    cryp_news_dict, score_list, sorted_description = sent_dict(cryp_news, description_list, descending = False)

    score_ = score(cryp_news)

    # # Bing NEWS
    # bing = bing_news("Ethereum")

    # coin_data = crypto_data('USDT_STR', "2018-01-01","2018-01-27", 14400)
    #
    # coin_json = coin_to_json(coin_data)

    percent_change_1h, percent_change_24h, percent_change_7d = changes_Stellar()

    context = {
        'title': 'Data',
        'news': cryp_news,
        'sentiment': score_list,
        'score': score_,
        'change_1': percent_change_1h,
        'change_24': percent_change_24h,
        'change_7': percent_change_7d
    }
    return render(request, 'crypto/stellar.html', context)
