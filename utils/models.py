# myproject/utils/models.py
# -*- coding: UTF-8 -*-

import urlparse

from django.db import models
#from django.contrib.sites.models import Site
from django.conf import settings
from django.utils.timezone import now as timezone_now
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import escape
from django.utils.safestring import mark_safe
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import fields # removed 'generic'
from django.core.exceptions import FieldError

class UrlMixin(models.Model):
    """
    A replacement for get_absolute_url()
    Models extending this mixin should have either
    get_url or get_url_path implemented.
    """
    class Meta:
        abstract = True
    
    def get_url(self):
        if hasattr(self.get_url_path, "dont_recurse"):
            raise NotImplementedError
        try:
            path = self.get_url_path()
        except NotImplementedError:
            raise
        website_url = getattr(settings, "DEFAULT_WEBSITE_URL", "http://127.0.01:8000")
        return website_url + path
    
    get_url.dont_recurse = True
    
    def get_url_path(self):
        if hasattr(self.get_url,"dont_recurse"):
            raise NotImplementedError
        try:
            url = self.get_url()
        except NotImplementedError:
            raise
        bits = urlparse.urlparse(url)
        return urlparse.urlparse(("","")+bits[2:])
    
    get_url_path.dont_recurse = True
    
    def get_absolute_url(self):
        return self.get_url_path()

class CreationModificationDateMixin(models.Model):
    """
    Abstract base class with a creation and modification date and time
    """
    
    created = models.DateTimeField(
                                   _("creation date and time"),
                                   editable = False,
                                   )
    modified = models.DateTimeField(
                                    _("modification date and time"),
                                    null=True,
                                    editable=False,
                                    )
    
    def save (self, *args, **kwargs):
        if not self.pk:
            self.created = timezone_now()
        else:
            # To ensure we have a creation date always we add this one
            if not self.created:
                self.created = timezone_now()
            
            self.modified = timezone_now()
            
        super(CreationModificationDateMixin, self).save(*args, **kwargs)
    
    save.alters_data = True
        
    class Meta:
        abstract = True

class MetaTagsMixin(models.Model):
    """
    Abstract base class for metatags in the <head> section
    """
    
    meta_keywords = models.CharField(
                                      _("Keywords"),
                                      max_length=255,
                                      blank=True,
                                      help_text=_("Separate Keywords by comma."),
                                      )
    meta_description = models.CharField(
                                        _("Description"),
                                        max_length=255,
                                        blank=True,
                                        )
    meta_author = models.CharField(
                                   _("Author"),
                                   max_length=255,
                                   blank=True,
                                   )
    meta_copyright = models.CharField(
                                      _("Charfield"),
                                      max_length=255,
                                      blank=True,
                                      )
    
    class Meta:
        abstract=True
    
    def get_meta_keywords(self):
        tag = u""
        if self.meta_keywords:
            tag = u'<meta name="keywords" content="%s" />\n' %\
                    escape(self.meta_keywords)
            return mark_safe(tag)

    def get_meta_description(self):
        tag = u""
        if self.meta_description:
            tag = u'<meta name="description" content="%s" />\n' %\
                    escape(self.meta_description)
            return mark_safe(tag)

    def get_meta_author(self):
        tag = u""
        if self.meta_author:
            tag = u'<meta name="author" content="%s" />\n' %\
                    escape(self.meta_author)
            return mark_safe(tag)

    def get_meta_copyright(self):
        tag = u""
        if self.meta_copyright:
            tag = u'<meta name="copyright" content="%s" />\n' %\
                    escape(self.meta_copyright)
            return mark_safe(tag)
    
    def get_meta_tags(self):
        return mark_safe(u"".join((
                                  self.get_meta_keywords(),
                                  self.get_meta_description(),
                                  self.get_meta_author(),
                                  self.get_meta_copyright(),
                                  )))

def object_relation_mixin_factory(
            prefix=None,
            prefix_verbose=None,
            add_related_name=None,
            limit_content_type_choices_to={},
            limit_object_choices_to={},
            is_required=False,
        ):
    
    """
    returns mixin class for generic foreign keys using
    "Content type-object id" with dynamic field names.
    This function is just a class Generator
    
    Parameters:
    prefix            : a prefix, which is added in front of the fields
    prefix_verbose    : a verbose name of the prefix, used to generate the
                        title for the field column of the content object in
                        the Admin.
    add_related_name  : a boolean value indicating, that a related name for
                        the generated content type foreign key should be added.
                        This value should be true, if you use more than one
                        ObjectRelationMixin in your model
    
    The fields are created like this:

    <<prefix>>_content_type :   Field name for the "content type"
    <<prefix>>_object_id :      Field name for the "object_id"
    <<prefix>>_content_object : Field name for the "content object"
    """
    
    if prefix:
        p = "%s_" % prefix
    else:
        p = ""
    
    content_type_field = "%scontent_type" % p
    object_id_field = "%sobject_id" % p
    content_object_field = "%scontent_object" % p
    
    class TheClass(models.Model):
        class Meta:
            abstract = True
    
    if add_related_name:
        if not prefix:
            raise FieldError("if add_related_name is set to True, "
                             "a prefix must be given")
        related_name = prefix
    else:
        related_name = None
        
    content_type = models.ForeignKey(
                    ContentType,
                    verbose_name=(prefix_verbose and
                                  _("%s's type (model)") % \
                                  prefix_verbose or
                                  _("Related object's type (model)")
                                  ),
                    related_name=related_name,
                    blank=not is_required,
                    null=not is_required,
                    help_text=_("Please select the type (model) for "
                                "the relation you want to build."),
                    limit_choices_to=limit_content_type_choices_to,
                    )
    
    object_id = models.CharField(
                    (prefix_verbose or _("Related object")),
                    blank=not is_required,
                    null=False,
                    help_text=_("Please enter the ID of the related object"),
                    max_length=255,
                    default=""
                    )
        
    object_id.limit_choices_to = limit_object_choices_to
    #can be retrieved by
    #Mymodel._meta.get_field("objectid").limit_choices_to
    content_object = fields.GenericForeignKey(
                            ct_field=content_type_field,
                            fk_field=object_id_field,
                            )
    
    TheClass.add_to_class(content_type_field, content_type)
    TheClass.add_to_class(object_id_field, object_id)
    TheClass.add_to_class(content_object_field, content_object)
    
    return TheClass