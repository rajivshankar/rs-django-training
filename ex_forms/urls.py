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
               ]