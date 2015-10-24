# myproject/ex_urls/views.py
# -*- coding: UTF-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def articles(request):
    return render(request,
                  'ex_urls/index.html',
                  {'year_list': (2003, 2004, 2005,),}
                  )

def redirect_to_year(request):
    year = 2006
    return HttpResponseRedirect(reverse('urls:news-year-archive', args=(year,)))

def special_case_2003(request):
    html = "<html><body>It is now only 2003</body></html>"
    return HttpResponse(html)

def year_archive(request, *args, **kwargs):
    try:
        html = "<html><body>It is key Year: %s</body></html>" %\
                (kwargs['year'],)
    except KeyError:
        html = "<html><body>It is Year: %s</body></html>" %\
                (args[0],)
    return HttpResponse(html)

def month_archive(request, *args, **kwargs):
    
    try:
        html = "<html><body>It is now key Year: %s Month: %s</body></html>" %\
         (kwargs['year'], kwargs['month'])
    except KeyError:
        html = "<html><body>It is now Year: %s Month: %s</body></html>" %\
         (args[0], args[1])
    return HttpResponse(html)

def day_archive(request, *args, **kwargs):
    try:
        html = "<html><body>It is now key"+\
        " Year: %s Month: %s Day: %s and arg3: %s</body></html>" %\
        (kwargs['year'], kwargs['month'], kwargs['day'], kwargs['extra'])
    except KeyError:
        html = "<html><body>It is now Year: %s Month: %s Day: %s</body></html>" %\
        (args[0], args[1], args[2])
    return HttpResponse(html)

