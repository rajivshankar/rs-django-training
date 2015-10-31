# my_project/ex_forms/urls.py
#-*- coding: UTF-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
               url(r'^get-name/$',
                   views.get_name,
                   name='get-name'),
               url(r'^success/$',
                   views.form_success,
                   name='forms-success'),
               url(r'^contact-us/$',
                   views.ContactFormView.as_view(),
                   name='contact-us'),
               url(r'^author/$',
                   views.AuthorFormView.as_view(),
                   name='author'),
               url(r'^book/$',
                   views.BookFormView.as_view(),
                   name='book'),
               ]