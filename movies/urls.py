# myproject/movies/urls.py
# _*_ coding: UTF-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
               url(r'^list/$',
                   views.movie_list,
                   name='movie-list'),
               ]