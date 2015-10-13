# myproject/polls/models.py
# -*- coding: UTF-8 -*-

from django.db import models
import datetime
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField("Question Text", max_length=200)
    pub_date = models.DateTimeField("Date Published")
    
    def __unicode__(self):        
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= now - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Recently Published'


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choices_text = models.CharField("Choices", max_length=200)
    votes = models.IntegerField("Votes", default=0)

    def __unicode__(self):        
        return self.choices_text

