'''
Fichier regroupant toute les URL des différentes vues de l'App
Django est très flexible avec les URL

https://docs.djangoproject.com/fr/3.1/topics/http/urls/
https://docs.djangoproject.com/fr/3.1/ref/urls/
'''
from django.conf.urls import url

from . import views

app_name='store'

urlpatterns = [
    url(r'^$', views.listing, name='listing'),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^search/$', views.search, name='search'),
]