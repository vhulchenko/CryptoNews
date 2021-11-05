from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import CoinSerializer
from .models import Coin


class CoinViewSet(viewsets.ModelViewSet):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer
