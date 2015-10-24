# my_project/ex_aggregation/models.py
# -*- coding: UTF-8 -*-

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    
    def __unicode__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=300)
    num_awards = models.IntegerField("Number of Awards")

    def __unicode__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    Publisher = models.ForeignKey(Publisher)
    pubdate = models.DateField("Published Date")

    def __unicode__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)
    registered_users = models.PositiveIntegerField()

    def __unicode__(self):
        return self.name
