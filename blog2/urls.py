from django.urls import path
from . import views

app_name = 'blog2'

urlpatterns = [
    path('', views.forumavisos, name='forumavisos'), # '', include configurado em urls.py do mysite
]
