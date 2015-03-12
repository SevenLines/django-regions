from django.conf.urls import patterns, url

__author__ = 'm'


urlpatterns = patterns('regions.views',
    url(r'add/$', 'add'),
    url(r'(?P<region_id>[0-9]+)/update/$', 'update'),
    url(r'$', 'index')
)