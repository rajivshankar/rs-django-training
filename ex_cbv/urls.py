# myproject/ex_cbv/urls.py
# -*- coding: UTF-8 -*-

from django.conf.urls import url, include
from . import views

urlpatterns = [
               url(r'^about/$',
                   views.AboutView.as_view(),
                   name='about',
                   ),
#                url(r'^books/$',
#                    views.BooklListView.as_view()
#                    ),
               url(r'^greeting/$',
                   views.GreetingView.as_view()
                   ),
               url(r'^howdy/$',
                   views.GreetingView.as_view(greeting='Howdy Stranger!')
                   ),
               url(r'^publishers/$',
                   views.PublisherList.as_view(),
                   name='publisher_list',
                   ),
               url(r'^publisher/(?P<pk>[0-9]+)/$',
                   views.PublisherDetail.as_view(),
                   name='publisher_detail',
                   ),
               url(r'^authors/$',
                   views.AuthorList.as_view(),
                   name='author_list',
                   ),
               url(r'^author/(?P<pk>[0-9]+)/$',
                   views.AuthorDetail.as_view(),
                   name='author_detail',
                   ),
               url(r'^book/(?P<pk>[0-9]+)/$',
                   views.BookDetail.as_view(),
                   name='book_detail',
                   ),
               url(r'^books/$',
                   views.BookList.as_view(),
                   name='book_list',
                   ),
                url(r'^contactus/$',
                    views.ContactView.as_view(),
                    name='contactus',
                    ),
                url(r'^person/',
                    include([
                            url(r'^all/$',
                                views.PersonList.as_view(),
                                name='person_list',
                                ),
                            url(r'^(?P<pk>[0-9]+)/$',
                                views.PersonDetail.as_view(),
                                name='person_detail',
                                ),
                            url(r'^create/$',
                                views.PersonCreate.as_view(),
                                name='person_create',
                                ),
                            url(r'^(?P<pk>[0-9]+)/update/$',
                                views.PersonUpdate.as_view(),
                                name='person_update',
                                ),
                            url(r'^(?P<pk>[0-9]+)/delete/$',
                                views.PersonDelete.as_view(),
                                name='person_delete',
                                ),
                            ])
                       ),
               
               ]