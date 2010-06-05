from django.contrib.auth.views import login, logout
from django.conf.urls.defaults import *
from mysite.views import hello, current_datetime, hours_ahead
from mysite.views import my_homepage_view


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', my_homepage_view), 
    (r'^hello/$', hello),
    (r'^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    # ...
    (r'^accounts/login/$',  login),
    (r'^accounts/logout/$', logout),
    )
