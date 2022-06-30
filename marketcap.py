import requests,time
from pycoingecko import CoinGeckoAPI as dark
coin = dark()
cakee = coin.get_price(ids='pancakeswap', vs_currencies='idr')
cake = str(cakee).split("idr': ")[1].split("}")[0]