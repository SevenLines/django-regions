from django.conf.urls import patterns, url

__author__ = 'm'


urlpatterns = patterns('regions.views',
    url(r'add/$', 'add'),
    url(r'$', 'index')
)