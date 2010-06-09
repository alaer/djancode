# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import Http404, HttpResponse
import datetime


def my_homepage_view(request):
    return HttpResponse("My_Home_Page")
