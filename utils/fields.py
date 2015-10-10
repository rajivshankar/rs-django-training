# myproject/
# -*- coding: UTF-8 -*-

from django.conf import settings
from django.db import models
from django.utils.translation import get_language
from django.utils.translation import string_concat
from django.utils.encoding import force_unicode
from django.utils.translation import ugettext_lazy as _

class MultilingualCharField(models.CharField):
    def __init__(self, verbose_name=None, **kwargs):
        
        self._blank = kwargs.get('blank', False)
        self._editable = kwargs.get('editable', True)
        
        # inits for the needed dummy field (see below)
        kwargs['editable'] = False
        kwargs['null'] = True
        kwargs['blank'] = self.blank
        super(MultilingualCharField, self).__init__(verbose_name, **kwargs)
    
    def contribute_to_class(self, cls, name, virtual_only=False):
       
        # generate language specific fields dynamically
        if not cls.meta.abstract:
            for lang_code, lang_name in settings.LANGUAGES:
                if lang_code == settings.LANGUAGE_CODE:
                    _blank = self._blank
                else:
                    _blank = True
                
                try:
                    # the field shouldn't be added (for south)
                    cls.meta.get_field("%s_%s" % (name, lang_code))
                except models.FieldDoesNotExist:
                    pass
                else:
                    continue
                
                localised_field = models.CharField(
                    string_concat(self.verbose_name, u"(%s)" % lang_code),
                    name=self.name,
                    primary_key=self.primary_key,
                    max_length=self.max_length,
                    unique=self.unique,
                    blank=_blank,
                    null=False,
                    # null value shoud be avoided for text-based fields
                    db_index=self.db_index,
                    rel=self.rel,
                    default=self.default or "",
                    editable=self.editable,
                    serialize=self.serialize,
                    choices=self.choices,
                    help_text=self.help_text,
                    db_column=None,
                    db_tablespace=self.db_tablespace,
                )
                localised_field.contribute_to_class(
                                        cls, 
                                        "%s_%s" % (name, lang_code),
                )
                
        super(MultilingualCharField, self).contribute_to_class(
                                    cls, name, virtual_only=True
        )
                
        def translated_value(self):
            language = get_language()
            val = self.__dict__["%s_%s" % (name, language)]
            if not val:
                val = self.__dict__["%s_%s" % (name, settings.LANGUAGE_CODE)]
            return val
        
        setattr(cls, name, property(translated_value))

class MultilingualTextField(models.TextField):
    def __init__(self, verbose_name=None, **kwargs):
        
        self._blank = kwargs.get('blank', False)
        self._editable = kwargs.get('editable', True)
        
        # inits for the needed dummy field (see below)
        kwargs['editable'] = False
        kwargs['null'] = True
        kwargs['blank'] = self.blank
        super(MultilingualTextField, self).__init__(verbose_name, **kwargs)
    
    def contribute_to_class(self, cls, name, virtual_only=False):
       
        # generate language specific fields dynamically
        if not cls.meta.abstract:
            for lang_code, lang_name in settings.LANGUAGES:
                if lang_code == settings.LANGUAGE_CODE:
                    _blank = self._blank
                else:
                    _blank = True
                
                try:
                    # the field shouldn't be added (for south)
                    cls.meta.get_field("%s_%s" % (name, lang_code))
                except models.FieldDoesNotExist:
                    pass
                else:
                    continue
                
                localised_field = models.TextField(
                    string_concat(self.verbose_name, u"(%s)" % lang_code),
                    name=self.name,
                    primary_key=self.primary_key,
                    max_length=self.max_length,
                    unique=self.unique,
                    blank=_blank,
                    null=False,
                    # null value shoud be avoided for text-based fields
                    db_index=self.db_index,
                    rel=self.rel,
                    default=self.default or "",
                    editable=self.editable,
                    serialize=self.serialize,
                    choices=self.choices,
                    help_text=self.help_text,
                    db_column=None,
                    db_tablespace=self.db_tablespace,
                )
                localised_field.contribute_to_class(
                                        cls, 
                                        "%s_%s" % (name, lang_code),
                )
                
        super(MultilingualCharField, self).contribute_to_class(
                                    cls, name, virtual_only=True
        )
                
        def translated_value(self):
            language = get_language()
            val = self.__dict__["%s_%s" % (name, language)]
            if not val:
                val = self.__dict__["%s_%s" % (name, settings.LANGUAGE_CODE)]
            return val
        
        setattr(cls, name, property(translated_value))