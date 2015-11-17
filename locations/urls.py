# myproject/locations/urls.py
# -*- coding: UTF-8 -*-

from django.conf.urls import url
from django.views.generic import ListView
from .models import Location
from django.views.generic import DetailView

urlpatterns =   [
                 url(r'^$',
                     ListView.as_view(model=Location),
                     name='list'
                     ),
                 url(r'^(?P<pk>[0-9]+)/$',
                     DetailView.as_view(model=Location),
                     name='detail'
                     ),
                 ]
