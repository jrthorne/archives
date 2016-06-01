from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView, RedirectView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(url='archives')),
    url(r'^archives/', include('archives.urls')), #direct_to_template, {'template': 'index.html'}),
    url(r'^survey/', include('survey.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
