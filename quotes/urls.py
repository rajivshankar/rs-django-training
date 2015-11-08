# myproject/quotes/urls.py
# -*- coding: UTF-8 -*-

from django.conf.urls import url
from .views import add_quote
from django.views.generic.base import TemplateView

urlpatterns = [
               url(r'^change',
                   add_quote,
                   name='change-quote',
                   ),
               url(r'success',
                   TemplateView.as_view(template_name='quotes/success.html'),
                   name='success',
                   ),
               ]