# myproject/movies/urls.py
# _*_ coding: UTF-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
               url(r'^$',
                   views.MovieListView.as_view(),
                   name="movie-list"),
               url(r'^list/$',
                   views.movie_list,
                   name='movie-list-2'),
               ]