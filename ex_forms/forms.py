# my_project/ex_forms.forms.py
# -*- coding: UTF-8 -*-

from django import forms
from django.forms.utils import ErrorList
from .models import Author, Book
from django.utils.translation import ugettext_lazy as _
from ex_forms.models import TITLE_CHOICES

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your Name', max_length=100)

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
    error_css_class = 'error'
    required_css_class = 'required'
    
    def clean(self):
        cleaned_data = super(ContactForm,self).clean()
        
        cc_myself = cleaned_data.get('cc_myself')
        subject = cleaned_data.get('subject')
        
        if cc_myself and subject:
            if "help" not in subject:
#                 raise forms.ValidationError(
#                         "Did not send for help despite cc'ing myself",
#                         "CC'ing yourself.",
#                         )
                msg = "Must put 'help' in the subject whilst cc'ing yourself"
                self.add_error('cc_myself', msg)
                self.add_error('sender', msg)
                

class DivErrorList(ErrorList):
    def __unicode__(self):
        return self.as_divs()
    
    def as_divs(self):
        if not self: return''
        return '<div> class="errorlist">%s</div>' %\
             ''.join(['<div class="error">%s</div>' % e for e in self])


# ModelForm exercises

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'title', 'birth_date']
        widgets = {
                   'name': forms.Textarea(attrs={'cols': 80,
                                                 'rows':20,
                                                 }),
                   }
        help_texts = {'name': _("ENter the name"),
                      }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'authors']

class AuthorFormSet():
    name = forms.CharField(max_length=100)
    title = forms.CharField(max_length=3,
                            widget=forms.Select(choices=TITLE_CHOICES))
    birth_date = forms.DateField(required=False)