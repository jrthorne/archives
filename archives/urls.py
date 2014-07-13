from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from django.conf.urls.static import static
from django.views.generic.simple import redirect_to, direct_to_template

from archives import views
from archives.models import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'archeologist.views.home', name='home'),
    

	url(r'^$', 
		ListView.as_view(
			queryset=historical_site.objects.all(),
			context_object_name='siteList',
			template_name='archives/index.html')),
			
    url(r'^(?P<pk>\d+)/$',
    		DetailView.as_view(
			model=historical_site,
			template_name='archives/relic_list.html')),
	 url(r'^add/(\d+)/$', views.relicAdd),
)
