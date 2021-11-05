from django.db import models

class Coin(models.Model):
    coin_id = models.PositiveIntegerField(verbose_name='Coin Id')
    name = models.CharField(max_length=30, verbose_name='Name')
    symbol = models.CharField(max_length=30, verbose_name='Symbol')
    twitter = models.URLField(verbose_name='Twitter')
    medium = models.URLField(verbose_name='Medium')