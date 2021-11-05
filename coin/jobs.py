import threading
from .models import Coin
from main import settings
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

def countSeconds():
    print('Started')
    getCoins()

def getCoins():
    threading.Timer(300, countSeconds).start()
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': '5',
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': settings.env('COIN_MARKET_KEY'),
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
