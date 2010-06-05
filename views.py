# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import Http404, HttpResponse
import datetime


def hello(request):
    return HttpResponse("qwerty2")

def my_homepage_view(request):
    return HttpResponse("My_Home_Page")

def current_datetime(request):
    now = datetime.datetime.now()
    """"
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)
    """
    return render_to_response('current_datetime.html', {'current_date': now})


def hours_ahead(request, offset):
    """ If URL /time/plus/3/, Then offset ===>3'    

    """
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)