# my_project/ex_queries/models.py
# -*- coding: UTF-8 -*-

from django.db import models

class Blog(models.Model):
    name = models.CharField("blog name", max_length=100)
    tagline = models.TextField(null=True,
                               blank=True,
                               default=None
                               )
    
    def __unicode__(self):
        return self.name

class Author(models.Model):
    name = models.CharField("author name", max_length=50)
    email = models.EmailField(null=True,
                              blank=True,
                              default=None
                              )
    
    def __unicode__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField(null=True,
                               blank=True,
                               default=None
                               )
    pub_date = models.DateField(null=True,
                               blank=True,
                               default=None
                               )
    mod_date = models.DateField(null=True,
                               blank=True,
                               default=None
                               )
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField(default=0)
    n_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(null=True,
                               blank=True,
                               default=None
                               )
    
    def __unicode__(self):
        return self.headline
    
    class Meta:
        verbose_name_plural = 'entries'