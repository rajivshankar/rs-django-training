# my_project/ex_forms/views.py
# -*- coding: UTF-8 -*-

from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import NameForm

def form_success(request):
    html = "<html><body><a href=\'" +\
     reverse('forms:get-name') \
     + "\'>Success</a><body></html>"
    
    return HttpResponse(html)


def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('forms:forms-success'))
    else:
        form = NameForm()
        
    return render_to_response('ex_forms/name.html',
                              context={'form':form},
                              context_instance=RequestContext(request),
                            )
