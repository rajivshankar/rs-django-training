# myproject/quotes/views.py
# -*- coding: UTF-8 -*-

from django.shortcuts import render, redirect
from .forms import InspirationQuoteForm
from django.core.urlresolvers import reverse

def add_quote(request):
    if request.method == 'POST':
        form = InspirationQuoteForm(
                                    data=request.POST,
                                    files=request.FILES,
                                    )
        if form.is_valid():
            quote = form.save()
            return redirect(reverse(("quotes:success")))
    else:
        form = InspirationQuoteForm()
    
    return render(request,
                  "quotes/change_quote.html",
                  {'form': form})