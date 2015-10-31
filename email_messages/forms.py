# my_project/email_messages/forms.py
# -*- coding: UTF-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.models import User

class MessageForm(forms.Form):
    recipient = forms.ModelChoiceField(
                                       label=_("Recipient"),
                                       queryset=User.objects.all(),
                                       required=True,
                                       )
    message = forms.CharField(
                              label=_("Message"),
                              widget=forms.Textarea,
                              required=True,
                              )
    
    def __init__(self, request, *args, **kwargs):
        super (MessageForm, self).__init__(*args, **kwargs)
        self.request = request
        self.fields['recipient'].queryset = \
            self.fields['recipient'].queryset.\
            exclude(pk=request.user.pk)
    
    def save(self):
        cleaned_data = self.cleaned_data
        send_mail(subject=_("A message from %s" % self.request.user),
                  message = cleaned_data['message'],
                  from_email = self.request.user.email,
                  recipient_list=[cleaned_data['recipient'].email],
                  fail_silently=True)