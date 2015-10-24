# my_project/ex_queries/admin.pu
#-*- coding: UTF-8 -*-

from django.contrib import admin
from .models import Author, Blog, Entry

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email',]

class BlogAdmin(admin.ModelAdmin):
    list_display = ['name', 'tagline',]

admin.site.register(Author, AuthorAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Entry)
