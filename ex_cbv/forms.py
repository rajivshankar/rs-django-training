# myproject/ex_cbv/forms.py
# -*- coding:UTF-8 -*-

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
    
    def send_email(self):
        pass
