# myproject/myauth/views.py
# -*- coding: UTF-8 -*-

from django.shortcuts import render
from .forms import MyAuthenticateForm
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy

class UserLoginForm(FormView):
    template_name = "myauth/login.html"
    form_class = MyAuthenticateForm
    success_url = '/user/login-success'
        