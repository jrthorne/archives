from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from django.conf.urls.static import static
from django.views.generic.simple import redirect_to, direct_to_template

from archives import views
from archives.models import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'archeologist.views.home', name='home'),
    

	url(r'^$', views.siteList),		
    url(r'^(\d+)/$', views.relicList), 
	url(r'^add/(\d+)/$', views.relicAdd),
)
