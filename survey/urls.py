
from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = patterns('survey.views',
	# Examples:
	url(r'^$', 'Index', name='home'),
	url(r'^(?P<id>\d+)/$', 'SurveyDetail', name='survey_detail'),
    url(r'^confirmPre/[0-9]{4}/$', 'ConfirmPre', name='ConfirmPre'),
    url(r'^confirmPost/[0-9]{4}/$', 'ConfirmPost', name='ConfirmPost'),

)


