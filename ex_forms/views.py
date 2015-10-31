# my_project/ex_forms/views.py
# -*- coding: UTF-8 -*-

from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import FormView

from .forms import NameForm, ContactForm, DivErrorList
from .forms import AuthorForm, BookForm 

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

class ContactFormView(FormView):
    template_name = 'ex_forms/contact_form.html'
    form_class = ContactForm
    success_url = '/forms/success/' #reverse('forms:forms-success')

class AuthorFormView(FormView):
    template_name = 'ex_forms/author_form.html'
    form_class = AuthorForm
    success_url = '/forms/success/' #reverse('forms:forms-success')
    
    def form_valid(self, form):
        form.save()
        return super(AuthorFormView, self).form_valid(form)

class BookFormView(FormView):
    template_name = 'ex_forms/book_form.html'
    form_class = BookForm
    success_url = '/forms/success/' #reverse('forms:forms-success')

    def form_valid(self, form):
        form.save()
        return super(BookFormView, self).form_valid(form)
