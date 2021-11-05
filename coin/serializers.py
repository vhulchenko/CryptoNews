from .models import Coin
from rest_framework import serializers


class CoinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coin
        fields = ['id', 'coin_id', 'name', 'symbol', 'twitter', 'medium']
