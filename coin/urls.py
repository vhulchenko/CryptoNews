from django.urls import path, include
from rest_framework import routers
from . import views
from . import jobs

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

router = routers.DefaultRouter()
router.register(r'list', views.CoinViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

#jobs.getCoinInfo()