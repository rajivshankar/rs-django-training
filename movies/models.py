# myproject/movies/models.py
# -*- coding: UTF-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

RATING_CHOICES = (
                  (1, u'*'),
                  (2, u'**'),
                  (3, u'***'),
                  (4, u'****'),
                  (5, u'*****'),
                )

class Genre(models.Model):
    title = models.CharField(_("Title"), max_length=100)
    
    def __unicode__(self):
        return self.title

class Director(models.Model):
    first_name = models.CharField(_("First Name"), max_length=40)
    last_name = models.CharField(_("Last Name"), max_length=40)
    
    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

class Actor(models.Model):
    first_name = models.CharField(_("First Name"), max_length=40)
    last_name = models.CharField(_("Last Name"), max_length=40)
    
    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

class Movie(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    genres = models.ManyToManyField(Genre, blank=True)
    directors = models.ManyToManyField(Director, blank=True)
    actors = models.ManyToManyField(Actor, blank=True)
    rating = models.PositiveIntegerField(_("Rating"), choices=RATING_CHOICES)
    
    def __unicode__(self):
        return self.title
