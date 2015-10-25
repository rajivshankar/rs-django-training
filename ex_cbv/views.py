# my_project/ex_cbv/views.py
# -*- coding:UTF-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.views.generic import View
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

#from ex_aggregation.models import Book

from .models import Publisher, Book, Author, Person
from .forms import ContactForm
from django.contrib.messages.api import success

class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form
    Must be used with an object-based FormView (e.g. CreateView)
    """
    
    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response
    
    def form_valid(self, form):
        # We make sure to call the pafrent's form_valid() because
        # it might do some processing (in case of CreateView, it will
        # call form_save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {'pk': self.object.pk,}
            return JsonResponse(data)
        else:
            return response
    

class AboutView(TemplateView):
    template_name = 'ex_cbv/about.html'

class BooklListView(ListView):
    model = Book
    
    def head(self, *args, **kwargs):
        last_book = self.get_queryset().latest('publication_date')
        response = HttpResponse('')
        response['last-Modified'] = last_book.publication_date.\
                                    strftime('%a, %d, %b %Y %H:%M:%S GMT')
        return response
    
    def get(self, *args, **kwargs):
        last_book = self.get_queryset().latest('publication_date')
        html = '<head><body>Last_modified Time: %s</body></head>' %\
                last_book.publication_date.strftime('%a, %d, %b %Y %H:%M:%S GMT')
        return HttpResponse(html)

class GreetingView(View):
    greeting = 'Hello'
    
    def get(self, request):
        html = '<head><body>%s</body></head>' % self.greeting
        return HttpResponse(html)

class PublisherList(ListView):
    model = Publisher
    context_object_name = 'my_favourite_publishers'

class PublisherDetail(DetailView):
    model = Publisher
    context_object_name = 'selected_publisher'
    
    def get_context_data(self, **kwargs):
        context = super(PublisherDetail, self).get_context_data(**kwargs)
        p = self.object
        context['book_list'] = p.book_set.all()
        return context

class AuthorList(ListView):
    model = Author
    context_object_name = 'preferred_authors'

class AuthorDetail(DetailView):
    model = Author
    context_object_name = 'selected_author'

    def get_context_data(self, **kwargs):
        context = super(AuthorDetail, self).get_context_data(**kwargs)
        p = self.object
        context['book_list'] = p.book_set.all()
        return context
    
class BookList(ListView):
    model = Book

class BookDetail(DetailView):
    model = Book
    context_object_name = "selected_book"

class ContactView(FormView):
    template_name = 'ex_cbv/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('cbv:about')
    
    def form_valid(self, form):
        form.send_email()
        return super(ContactView, self).form_valid(form)

class PersonCreate(AjaxableResponseMixin, CreateView):
    model = Person
    fields = ['name']
    template_name_suffix = '_form_create'
    
    def get_context_data(self, **kwargs):
        context = super(PersonCreate, self).get_context_data(**kwargs)
        context ['action'] = 'create'
        return context

class PersonUpdate(UpdateView):
    model = Person
    context_object_name = 'person_detail'
    fields = ['name']
    template_name_suffix = '_form_update'
    
    def get_context_data(self, **kwargs):
        context = super(PersonUpdate, self).get_context_data(**kwargs)
        context ['action'] = 'update'
        return context

class PersonDelete(DeleteView):
    model = Person
    context_object_name = 'person_detail'
    success_url = reverse_lazy('cbv:person_list')
######
class PersonList(ListView):
    model = Person
    context_object_name = 'person_list'

class PersonDetail(DetailView):
    model = Person
    context_object_name = 'person_detail'
