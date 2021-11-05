import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

import django
django.setup()


from apscheduler.schedulers.blocking import BlockingScheduler
from coin import jobs


sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=30, jitter=30)
def timed_job():
    print('This job is run every 30 minutes.')

    jobs.getCoins()
    jobs.getCoinInfo()


@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
def scheduled_job():
    print('This job is run every weekday at 5pm.')


sched.start()
