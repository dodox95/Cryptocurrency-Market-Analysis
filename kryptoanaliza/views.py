# kryptoanaliza / views.py
from django.shortcuts import render
from pycoingecko import CoinGeckoAPI

def index(request):
    cg = CoinGeckoAPI()
    top_100_coins = cg.get_coins_markets(vs_currency='usd', order='market_cap_desc', limit=100)
    return render(request, 'index.html', {'top_100_coins': top_100_coins})


def coin_detail(request, coin_id):
    cg = CoinGeckoAPI()
    coin_data = cg.get_coin_by_id(id=coin_id)
    
    return render(request, 'coin_detail.html', {'coin_data': coin_data})
