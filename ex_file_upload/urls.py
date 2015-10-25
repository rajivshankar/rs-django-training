# myproject/ex_file_upload/urls.py
# -*- coding: UTF-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
              url(r'^upload/$',
                  views.upload_file,
                  name='upload'
                  ),
              url(r'^success/$',
                  views.UploadFileSuccess,
                  name='success'
                  ),
              ]