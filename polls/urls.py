# myproject/polls/url.py
# -*- CODING: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
              url(r'^$',
                  views.IndexView.as_view(),
                  name='index'
                ), # ex: /polls/
              url(r'^(?P<pk>[0-9]+)/$',
                  views.DetailView.as_view(),
                  name = 'detail'
                ), # ex: /polls/5/
              url(r'^(?P<pk>[0-9]+)/results/$',
                  views.ResultsView.as_view(),
                  name = 'results'
                ), # ex: /polls/5/results/
              url(r'^(?P<question_id>[0-9]+)/vote/$',
                  views.vote,
                  name = 'vote'
                ), # ex: /polls/5/vote/
            ]