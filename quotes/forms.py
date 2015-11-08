# myproject/quotes/forms.py
# -*- coding: UTF-8 -*-

from django import forms
from . import models

class InspirationQuoteForm(forms.ModelForm):
    class Meta:
        model = models.InspirationalQuote
        fields = '__all__'