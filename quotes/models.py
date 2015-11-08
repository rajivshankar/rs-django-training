# myproject/quotes/models.py
# -*- coding: UTF-8 -*-

import os

from django.db import models
from django.utils.timezone import now as timezone_now
from django.utils.translation import ugettext_lazy as _
from PIL.Image import Image

def upload_to(instance, filename):
    now = timezone_now()
    filename_base, filename_ext = os.path.splitext(filename)
    return 'quotes/%s%s' % (
                            now.strftime("%Y/%m/%Y%m%d%H%M%S"),
                            filename_ext.lower(),
                            )

class InspirationalQuote(models.Model):
    author = models.CharField(_("Author"), max_length=200)
    quote = models.TextField(_("Quote"))
    picture = models.ImageField(_("Picture"),
                                upload_to = upload_to,
                                blank=True,
                                null=True,
                                )
    
    class Meta:
        verbose_name = _("Inspiration Quote")
        verbose_name_plural = _("Inspiration Quotes")
    
    def __unicode__(self):
        return self.quote
    
    def save(self, *args, **kwargs):
        super(InspirationalQuote, self).save(*args, **kwargs)
        self.create_thumbnail()
    
    def create_thumbnail(self):
        from django.core.files.storage import default_storage as storage
        if not self.picture:
            return ""
        file_path = self.picture.name
        filename_base, filename_ext = os.path.split(file_path)
        thumbnail_file_path = "%s_thumbnail.jpg" % filename_base
        if storage.exists(thumbnail_file_path):
            # If thumbnail version exists, return its URL path
            return "exists"
        try:
            # resize the original image and 
            # return URL path of the thumbnail version
            f = storage.open(file_path, 'r')
            image = Image.open(f)
            width, height = image.size
            thumbnail_size = 50, 50
            
            if width > height:
                delta = width - height
                left = int(delta/2)
                upper = 0
                right = height + left
                lower = height
            else:
                delta = height - width
                left = 0
                upper = int(delta/2)
                rght = width
                lower = width + upper
                
            image = image.crop((left, upper, right, lower))
            image = image.resize(thumbnail_size, Image.ANTIALIAS)
            
            f_mob = storage.open(thumbnail_file_path, "w")
            image.save(f_mob, "JPEG")
            f_mob.close()
            return "Success"
        except:
            raise IOError
            return "error"
        
    def get_thumbnail_picture_url(self):
        from PIL import Image
        from django.core.files.storage import default_storage as storage
        
        if not self.picture:
            return ""
        file_path = self.picture.name
        filename_base, filename_ext = os.path.split(file_path)
        thumbnail_file_path = "%s_thumbnail.jpg" % filename_base
        if storage.exists(thumbnail_file_path):
            # if thumbnail version exists, return its URL path
            return storage.url(thumbnail_file_path)
        # return original as a fallback
        return self.picture.url