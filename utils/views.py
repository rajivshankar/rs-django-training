from datetime import datetime, timedelta
from django.shortcuts import render, render_to_response
from django.views.decorators.cache import cache_control
from django.template.context import RequestContext
from django.conf import settings

def csrf_failure(request, reason=""):
#     raise KeyError
    ctx = {'message': reason}
    return render_to_response("utils/csrf_fail_message.html", ctx)

@cache_control(public=True)
def render_js(request, cache=True, *args, **kwargs):
    response = render(request, *args, **kwargs)
    response["Content-Type"] = "application/javascript; charset=UTF-8"
    if cache:
        now = datetime.utcnow()
        response["Last-Modified"] = now.strftime("%a, %d %b %Y %H %M %S GMT")
        # cache in the browser for one month
        expires = now + timedelta(days=31)
        response["Expires"] = expires.strftime("%a, %d %b %Y %H %M %S GMT")
        response["Pragma"] = "No-Cache"
    
    return response