# myproject/bulletin_board/forms.py
# -*- coding: UTF-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext

from crispy_forms.helper import FormHelper
from crispy_forms import layout, bootstrap
from crispy_forms.layout import Field, Fieldset, Layout, HTML, Div, Submit
from crispy_forms.bootstrap import PrependedText, FormActions
from .models import Bulletin
from django.core.urlresolvers import reverse

class BulletinForm(forms.ModelForm):
    class Meta:
        model = Bulletin
        fields = ('bulletin_type', 'title', 'description',
               'contact_person', 'phone', 'email', 'image',)
        
    def __init__(self, *args, **kwargs):
        super(BulletinForm, self).__init__(*args, **kwargs)
        
        self.helper = FormHelper()
        self.helper.form_action = "bulletin-board:change-view"
        self.helper.form_method = "POST"
        

        self.fields['bulletin_type'].widget = forms.RadioSelect()
        #delete the empty choice for the type
        del self.fields['bulletin_type'].choices[0]
        
        self.helper.layout = Layout(
                Fieldset(
                    _("Main Data"),
                    Field("bulletin_type"),
                    Field("title",
                                  css_class="input-block-level"),
                    Field("description",
                                  css_class="input-block-level",
                                  rows="3"),
                    ),
                Fieldset(
                    _("Image"),
                    Field("image",
                                 css_class="input-block-level"),
                    HTML(u"{%load i18n %}"+\
                        u'<p class="help-block">{% trans "Available formats '+
                        u'are JPG, GIF, and PNG. Minimum size is 800 x 800 px." %}</p>'
                        ),
                    title=_("Image upload"),
                    css_id="image_fieldset",
                    ),
                Fieldset(
                    _("Contact"),
                    Field("contact_person",
                        css_class="input-block-level"),
                    Div(
                        PrependedText("phone",
                            """<span class="glyphicon glyphicon-earphone">
                            </span>""",
                            css_class="input-block-level"),
                        PrependedText("email","@",
                            css_class="input-block-level",
                            placeholder="contact@example.com"),
                        css_id="contact_info",
                        ),
                ),
                FormActions(
                            Submit('submit',
                                          _("Save"),
                                          css_class='btn-primary'),
                )
            )