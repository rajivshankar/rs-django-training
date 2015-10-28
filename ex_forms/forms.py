# my_project/ex_forms.forms.py
# -*- coding: UTF-8 -*-

from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your Name', max_length=100)
    