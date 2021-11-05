from main import settings


settings.configure()


from apscheduler.schedulers.blocking import BlockingScheduler
from coin.models import Coin
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=3, jitter=130)
def timed_job():
    print('This job is run every three minutes.')

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


@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
def scheduled_job():
    print('This job is run every weekday at 5pm.')


sched.start()
