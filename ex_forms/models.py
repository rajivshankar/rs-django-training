# my_project/ex_forms/models.py
# -*- coding: UTF:8 -*-

from django.db import models

TITLE_CHOICES = (
                 ('MR', 'Mr.'),
                 ('MRS', 'Mrs.'),
                 ('MS', 'Ms.'),
                 )

class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3,
                             choices = TITLE_CHOICES)
    birth_date = models.DateField(blank=True, null=True)
    
    def __unicode__(self):
        return self.name
    
class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    
    def __unicode__(self):
        return self.name