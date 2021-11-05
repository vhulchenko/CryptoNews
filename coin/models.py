from django.db import models

class Coin(models.Model):
    coin_id = models.PositiveIntegerField(verbose_name='Coin Id', unique=True)
    name = models.CharField(max_length=30, verbose_name='Name', unique=True)
    symbol = models.CharField(max_length=30, verbose_name='Symbol', unique=True)
    twitter = models.URLField()
    medium = models.URLField()

    def createOrUpdate(params):
        oldCoin = Coin.objects.all().filter(coin_id=params['id'])
        if oldCoin.count()==0:
            coin = Coin(coin_id=params['id'], name=params['name'], symbol=params['symbol'])
            coin.save()
        else:
            print('Need updates')
            print(oldCoin[0].name)
