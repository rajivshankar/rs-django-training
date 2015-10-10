# myproject/demo_app/models.py
# -*- coding: UTF-8 -*-

from django.db import models
from django.utils.translation import  ugettext_lazy as _
from django.core.urlresolvers import reverse

from utils.models import UrlMixin
from utils.models import object_relation_mixin_factory
from utils.fields import MultilingualCharField
from utils.fields import MultilingualTextField

class Idea(UrlMixin):
    title = MultilingualCharField(
                            _("Title"),
                             max_length=200
    )
    description = MultilingualTextField(
                            _("Description"),
                            blank=True,
    )
    
    class Meta:
        verbose_name = _("Idea")
        verbose_name_plural = _("Ideas")
    
    def __unicode__(self):
        return self.title
    #...
    def get_url_path(self):
        return reverse(
                       "Idea_details",
                       kwargs={
                               "idea_id": str(self.pk),
                               }
                       )

FavouriteObjectMixin = object_relation_mixin_factory(
                             is_required=True,
                             )

OwnerMixin = object_relation_mixin_factory(
                        prefix="Owner",
                        prefix_verbose=_("Owner"),
                        add_related_name=True,
                        limit_content_type_choices_to = {
                            'model__in': ('user', 'institution')
                            },
                        is_required=True,
                        )

class Like(FavouriteObjectMixin, OwnerMixin):
    class Meta:
        verbose_name = _("Like")
        verbose_name_plural = _("Likes")
        
    def __unicode__(self):
        return _(u"%(owner)s likes %(obj)s") % {
            'owner': self.owner_content_object,
            'obj': self.content_object,
            }