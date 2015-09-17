from django.conf.urls import patterns, url, include
from django.contrib import admin
admin.autodiscover()
from class_activity.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SJTU_CS04.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   	url(r'index$', index),
)
