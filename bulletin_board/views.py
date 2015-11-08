# myproject/bulletin_board/views.py
# -*- coding: UTF-8 -*-

from django.shortcuts import render, redirect
from .forms import BulletinForm
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic.edit import FormView

def bulletin_change(request):
    if request.method=="POST":
        form =  BulletinForm(request.POST, request.FILES)
        if form.is_valid():
            bulletin = form.save()
            return redirect(reverse("bulletin-board:success"))
    else:
        form = BulletinForm()
    
    return render(request,
                  "bulletin_board/change_form.html",
                  {'form': form})
