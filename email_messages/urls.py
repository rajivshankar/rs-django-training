# myproject/email_messages/urls.py
# -*- coding: UTF-8 -*-

from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
                url(r'^success/$',
                    TemplateView.as_view(
                            template_name="email_messages/success_page.html"),
                    name='message-success',
                    ),
                url(r'^new/$',
                    views.message_to_user,
                    name='message-to-user',
                    ),
                ]