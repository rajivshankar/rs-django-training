# my_projects/email_messages/views.py
# -*- coding: UTF-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect

from .forms import MessageForm

@login_required
def message_to_user(request):
    if request.method == 'POST':
        form = MessageForm(request, data=request.POST)
        if form.is_valid():
            #do something with the form
            return redirect("Message_to_user_done")
        else:
            form = MessageForm(request)
        
        return render(request,
                      "email_messages/message_to_user.html",
                      {'form': form})