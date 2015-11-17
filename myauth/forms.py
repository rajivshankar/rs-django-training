# myproject/myauth/forms.py
# -*- coding: UTF-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms import layout, bootstrap
from django.contrib.auth.forms import AuthenticationForm

class MyAuthenticateForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(MyAuthenticateForm, self).__init__(*args, **kwargs)
        
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        
        self.helper.layout = layout.Layout(
            layout.Fieldset(
                _("User Details"),
                layout.Field(_('username')),
                layout.Field(_('password')),
            ),
            bootstrap.FormActions(
                layout.Submit('submit', _("login")),
            )
        )