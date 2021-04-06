'''
Fichier regroupant toute les URL des différentes vues de l'App
Django est très flexible avec les URL

https://docs.djangoproject.com/fr/3.1/topics/http/urls/
https://docs.djangoproject.com/fr/3.1/ref/urls/
'''

from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.listing, name="Listing"),
    re_path(r'^(?P<album_id>[0-9]+)/$', views.detail),
    re_path(r'^search/$', views.search),
    ]