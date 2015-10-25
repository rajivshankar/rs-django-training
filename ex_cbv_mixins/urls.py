# myproject/ex_cbv_mixins/urls.py
# -*- coding: UTF-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
               url(r'^author/(?P<pk>[0-9]+)/interest/$',
                    views.RecordInterest.as_view(),
                    name='author-interest'),
               url(r'^publisher/(?P<pk>[0-9]+)/$',
                    views.PublisherDetail.as_view(),
                    name='publisher-detail'),
               ]