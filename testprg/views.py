# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse
from mysite.testprg.models import Publisher

def search_form(request):
    pub = Publisher.objects.get(id=1)
    return render_to_response('search_form.html',{ 
        'name'   :pub.name,
        'name2'  :pub.name2,
        'name3'  :pub.name3,
        'dtbirth':pub.dtbirth,
        'city'   :pub.city,
        'country':pub.country,
        'address':pub.address,
        'website':pub.website,
        'email'  :pub.email})
         
