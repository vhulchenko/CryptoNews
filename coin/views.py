from django.http import HttpResponse
from .models import Coin
from django.db import models

# Create your views here.

def list(request):
    return HttpResponse(Coin.objects.all())