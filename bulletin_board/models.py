# myproject/bulletin_board/models.py
# -*- coding: UTF-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

TYPE_CHOICES = (
                ('searching', _("Searching")),
                ('offering', _("Offering")),
            )

class Bulletin(models.Model):
    bulletin_type = models.CharField(_("Type"),
                                     max_length=20,
                                     choices=TYPE_CHOICES)
    title = models.CharField(_("Title"),
                             max_length=255)
    description = models.CharField(_("Description"),
                               max_length=300)
    
    contact_person = models.CharField(_("Contact person"),
                                      max_length=255)
    phone = models.CharField(_("Phone"),
                             max_length=200,
                             blank=True)
    email = models.EmailField(_("Email"), blank=True)
    
    image = models.ImageField(_("Image"),
                              max_length=255,
                              upload_to="bulletin_board/",
                              blank=True)
    
    class Meta:
        verbose_name = _("Bulletin")
        verbose_name_plural = _("Bulletins")
        ordering = ("title",)
    
    def __unicode__(self):
        return self.title
    