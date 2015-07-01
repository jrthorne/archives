from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'archeologist.views.home', name='home'),
    # url(r'^archeologist/', include('archeologist.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^archives/', include('archives.urls')), #direct_to_template, {'template': 'index.html'}),
    url(r'^study/', include('study.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
