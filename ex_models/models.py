# myproject/ex_models/models.py
# -*- coding: UTF-8 -*-

from django.db import models

class Person (models.Model):
    SHIRT_SIZES = (
                   ('S', 'Small'),
                   ('M', 'MEdium'),
                   ('L', 'Large'),
                   )
    first_name = models.CharField("first name", max_length=30)
    last_name = models.CharField("last name", max_length=30)
    birth_date = models.DateField("birthday ddmmyyyyy",
                                  blank=True,
                                  null=True,)
    
    shirt_size = models.CharField(
                                  "shirt size",
                                  max_length=1,
                                  choices = SHIRT_SIZES,
                                  null=True,
                                  blank=True,
                                  default=None
                                  )
    
    class Meta:
        ordering = ["last_name",]
        verbose_name_plural = 'People'
    
    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)
    
    def baby_boomer_status(self):
        """Returns the person's baby-boomer status"""
        import datetime
        if self.birth_date < datetime.date(1945, 8,1):
            return "Pre-boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
            return "Baby Boomer"
        else:
            return "Post-boomer"
    
    def _get_full_name(self):
        """Returns the person's full name"""
        return "%s %s" % (self.first_name, self.last_name)
    full_name = property(_get_full_name)#
    
    def save(self, *args, **kwargs):
        if self.full_name == 'Yoko Ono':
            return
        else:
            super(Person, self).save(*args, **kwargs)

class Group(models.Model):
    name = models.CharField("group name", max_length=20)
    members = models.ManyToManyField(Person, through='Membership')
    
    def __unicode__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person)
    group = models.ForeignKey(Group)
    date_joined = models.DateField(verbose_name="date joined")
    invite_reason = models.CharField(max_length=64)
    

class Musician (Person):
    instrument = models.CharField("instrument", max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, verbose_name="artist name")
    name = models.CharField("name", max_length=100)
    release_date = models.DateField(verbose_name="release date")
    num_stars = models.IntegerField(verbose_name="rating")

class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

class Manufacturer(models.Model):
    name = models.CharField("manufacturer's name", max_length=100)

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer)
    name = models.CharField("car model name", max_length=100)

#MUlti-table inheritance
class Place(models.Model):
    name = models.CharField("Place's name", max_length=50)
    address = models.CharField("Place's address", max_length=80)
    
    def __unicode__(self):
        return "%s: %s" % (self.name, self.address)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s: %s [serves pizza: %s], [serves hot dogs: %s]" %\
             (self.name, self.address, self.serves_pizza, self.serves_hot_dogs)

class Supplier(Place):
    customers = models.ManyToManyField(Place,
                                       related_name = "%(class)s_related",
                                       )
#Proxy models
class myPerson(Person):
    class Meta:
        ordering = ["-last_name"]
        proxy = True
    
    def do_something(self):
        pass

# Multiple Inheritance
class Article (models.Model):
    article_id = models.AutoField(primary_key=True)
    headline = models.CharField(max_length=50)
    body = models.TextField(default = None)
    
class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)

class BookReview(Book, Article):
    pass

