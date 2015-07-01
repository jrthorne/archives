###################################################################
FileName        = 'urls.py'
# By:            Nan JIN
# Date:            30-06-2015
# Description:     The archeologist project - Usability Testing
##################################################################

from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from django.conf.urls.static import static
from django.views.generic import TemplateView

from archives.models import *

urlpatterns = patterns('study.views',
    # Examples:
    # url(r'^$', 'archeologist.views.home', name='home'),
    
    url(r'^$', 'surveyList', name='study'),
    url(r'^(\d+)/$','questionnaire',name='questionnaire')
)
