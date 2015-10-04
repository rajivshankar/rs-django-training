# -*- code: UTF-8 -*-
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

SETTING1 = getattr(settings, "MYAPP1_SETTING1", u"default value")
MEANING_OF_LIFE = getattr(settings, "MYAPP1_MEANING_OF_LIFE", 42)
STATUS_CHOICES = getattr(settings,
                        "MYAPP1_STATUS_CHOICES",
                        (
                             ('draft', _('Draft')),
                             ('published', _('Published')),
                             ('not listed', _('Not Listed')),
                         )
                    )