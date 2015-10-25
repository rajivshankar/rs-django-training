# myproject/ex_cbv_mixins/views.py
# -*- coding: UTF-8 -*-

from django.shortcuts import render
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import View, ListView
from django.views.generic.detail import SingleObjectMixin

from ex_cbv.models import Author, Publisher

class RecordInterest (SingleObjectMixin, View):
    """
    Records the current user's interest in an author
    """
    
    model = Author
    
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseForbidden()
        
        # Look up the author we're interested in.
        self.object = self.get_object()
        # Actually record interest somehow here.
        
        return HttpResponseRedirect(reverse('cbv:author-detail',
                                             kwargs={'pk': self.object.pk}))

class PublisherDetail(SingleObjectMixin, ListView):
    paginate_by = 2
    template_name = 'ex_cbv_mixins/publisher_detail.html'
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Publisher.objects.all())
        return super(PublisherDetail, self).get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(PublisherDetail,
                        self).get_context_data(**kwargs)
        context ['publisher'] = self.object
        return context
    
    def get_queryset(self):
        return self.object.book_set.all()