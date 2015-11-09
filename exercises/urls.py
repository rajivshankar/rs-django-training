"""exercises URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
                url(r'^$',
                    TemplateView.as_view(template_name='home.html'),
                    name='home',
                    ),
                url(r'^polls/', include('polls.urls', 
                                        namespace='polls',
                                        app_name='polls',
                                        )
                    ),
                url(r'^publisher-polls/', include('polls.urls',
                                                namespace='publisher-polls',
                                                app_name='polls'
                                                )
                     ),
                url(r'^admin/', include(admin.site.urls)),
                url(r'^urls/', include('ex_urls.urls',
                                        namespace='urls', 
                                        app_name='urls')
                    ),
                url(r'^file/', include('ex_file_upload.urls',
                                        namespace='file_upload', 
                                        app_name='ex_file_upload')
                    ),
                url(r'^cbv/', include('ex_cbv.urls',
                                       namespace='cbv',
                                       app_name='ex_cbv')
                    ),
                url(r'^cbv-mixins/', include('ex_cbv_mixins.urls',
                                           namespace='cbv-mixins',
                                           app_name='ex_cbv_mixins')
                    ),
                url(r'^forms/', include('ex_forms.urls',
                                       namespace='forms',
                                       app_name='ex_forms')
                    ),
                url(r'^email/', include('email_messages.urls',
                                       namespace='email',
                                       app_name='email_messages')
                    ),
                url(r'^quotes/', include('quotes.urls',
                                         namespace='quotes',
                                         app_name='quotes')
                    ),
                url(r'^bulletin-board/', include('bulletin_board.urls',
                                                 namespace='bulletin-board',
                                                 app_name='bulletin_board')
                    ),
                url(r'^movies/', include('movies.urls',
                                         namespace='movies',
                                         app_name='movies')
                    ),
               ]