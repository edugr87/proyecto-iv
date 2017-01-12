from django.http import HttpResponse
import datetime

def current_datetime(request):
    now=datetime.datetime.now()
    html="<html><body>son las %S.</body></html>"
    return HttpResponse(html)
