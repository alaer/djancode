# -*- coding: utf-8 -*-
#from django.contrib.auth.views import login, logout
from django.conf.urls.defaults import *
from django.contrib import admin
from mysite.views import my_homepage_view
from mysite.testprg import views

###

urlpatterns = patterns('',
    (r'^$', my_homepage_view), 
    # ...
    (r'^admin/', include(admin.site.urls)),
    (r'^search-form/$',views.search_form),
    )
