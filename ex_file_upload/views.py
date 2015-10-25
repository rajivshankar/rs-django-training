# myproject/ex_file_upload/voews.py
# -*- coding: UTF-8 -*-

from django.shortcuts import render_to_response, render, RequestContext
from django.http import HttpResponseRedirect, HttpResponse, Http404
from .forms import UploadFileForm
from django.core.urlresolvers import reverse

def UploadFileSuccess(request):
#     return HttpResponse("<html><body>SUccess</body></html>")
#     return render_to_response('ex_file_upload/success.html', RequestContext(request, {}))
    return render(request, 'ex_file_upload/success.html')

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            return HttpResponseRedirect(reverse('file_upload:success'))
    else:
        form = UploadFileForm()
    return render_to_response(
                              'ex_file_upload/upload.html',
                              {'form': form},
                              context_instance=RequestContext(request),
                              )

def csrf_failure(request, reason=""):
    raise KeyError