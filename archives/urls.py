from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from django.conf.urls.static import static
from django.views.generic import TemplateView

from archives.models import *

urlpatterns = patterns('archives.views',
    # Examples:
    # url(r'^$', 'archeologist.views.home', name='home'),
    

    url(r'^$', 'siteList', name='siteList'),        
    url(r'^(\d+)/$', 'relicList', name='relicList'), 
    url(r'^add/(\d+)/$', 'relicAdd', name='relicAdd'),
    url(r'^mod/(\d+)/$', 'relicMod', name='relicMod'),
    url(r'^login/$', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),
)
