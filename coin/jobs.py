from .models import Coin
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


def getCoins():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': '5',
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '0cfff5bf-0a32-4c50-87cd-ed9cc565653c',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        for item in data['data']:
            Coin.createOrUpdate(item)

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


def getCoinInfo():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info'
    ids = ''
    allCoins = Coin.objects.all()
    for coin in allCoins:
        ids = ids + str(coin.coin_id) + ','
    parameters = {
        'id': ids[:-1]
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '0cfff5bf-0a32-4c50-87cd-ed9cc565653c',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)['data']
        for coin in allCoins:
            if str(coin.coin_id) in data:
                Coin.update(coin, data[str(coin.coin_id)])
                print("this will execute")

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
