# myproject/myauth/urls/py
# -*- coding: UTF-8 -*-

from django.conf.urls import url
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .views import UserLoginForm

urlpatterns =   [
                 url(r'^login-success',
                     TemplateView.as_view(
                        template_name="myauth/login_success.html"),
                     name='login-success'),
                 url(r'^login',
                     UserLoginForm.as_view(),
                     name='login'),
                 ]