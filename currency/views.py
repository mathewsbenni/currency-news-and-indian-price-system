from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    import requests
    import json
    price_request=requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=ETH,BTC,USD,EUR&tsyms=INR')
    price=json.loads(price_request.content)
    news_request=requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api=json.loads(news_request.content)
    return render(request,'currency/home.html',{'api':api,'price':price})
