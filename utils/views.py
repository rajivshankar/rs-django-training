from django.shortcuts import render_to_response

def csrf_failure(request, reason=""):
#     raise KeyError
    ctx = {'message': reason}
    return render_to_response("utils/csrf_fail_message.html", ctx)
