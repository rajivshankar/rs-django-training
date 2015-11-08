# myproject/bulletin_board/urls.py
# -*- coding: UTF-8 -*-

from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
from .forms import BulletinForm
from django.core.urlresolvers import reverse_lazy

urlpatterns = [
               url(r'^change/$',
                  views.bulletin_change,
                  name='change'
                ),
               url(r'^changeview/$',
                  views.FormView.as_view(
                    template_name = "bulletin_board/change_form.html",
                    form_class = BulletinForm,
                    success_url = reverse_lazy("bulletin-board:success"),
                    ),
                  name='change-view'
                ),
               url(r'^success/$',
                   TemplateView.as_view(
                            template_name="bulletin_board/success.html"),
                   name='success'
                ),
            ]