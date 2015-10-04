# myproject/myapp1/models.py
# -*- coding: UTF-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.models import UrlMixin
from utils.models import CreationModificationDateMixin
from utils.models import  MetaTagsMixin

from .app_settings import STATUS_CHOICES

class NewsArticle (models.Model):
    #...
    status = models.CharField(
                              _("Status"),
                              max_length=20,
                              choices=STATUS_CHOICES,
                              )
    
class Idea(UrlMixin, CreationModificationDateMixin, MetaTagsMixin):
    title = models.CharField(_("Title"),
                             max_length=200
                             )
    content = models.TextField(_("Content"))
    
    class Meta:
        verbose_name = _("Idea")
        verbose_name_plural = _("Ideas")
    
    def __unicode__(self):
        return self.title