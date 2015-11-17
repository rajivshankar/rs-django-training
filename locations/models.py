# myproject/locations/models.py
# -*- coding: UTF-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Location(models.Model):
    title = models.CharField(_("Title"), max_length=100)
    small_image = models.ImageField(_("Small Image"))
    medium_image = models.ImageField(_("Medium Image"))
    large_image = models.ImageField(_("Large Image"))
    latitude = models.FloatField(_("Latitude"), blank=True, null=True)
    longitude = models.FloatField(_("Longtude"), blank=True, null=True)
    
    def __unicode__(self):
        return self.title
    