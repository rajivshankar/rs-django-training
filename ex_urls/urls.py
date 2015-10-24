# myproject/ex_urls/urls.py
# -*- coding: UTF-8 -*-

from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
               url(r'^articles/$', views.articles),
               url(r'^articles/redirect/$', views.redirect_to_year),
               url(r'^articles/2003/$', views.special_case_2003),
               url(r'articles/([0-9]{4})/$',
                   views.year_archive,
                   name='news-year-archive'),
#                url(r'articles/([0-9]{4})/([0-9]{2})/$', 
#                    views.month_archive
#                 ),
#                url(r'articles/([0-9]{4})/([0-9]{2})/([0-9]{2})/$',
#                    views.day_archive
#                 ),
               url(r'^articles/(?P<year>[0-9]{4})/',
                    include(
                            [
                            url(r'^$',
                                views.year_archive,
                                
                            ),
                            url(r'^(?P<month>[0-9]{2})/',
                            include(
                                    [
                                    url(r'^$', views.month_archive),
                                    url(r'^(?P<day>[0-9]{2})/$',
                                        views.day_archive,
                                        {'extra':'arg3'}
                                        ),
                                     ]
                                    ),
                                ),
                             ]
                            )
                    ),
               ]