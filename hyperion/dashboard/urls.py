from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'hyperion.dashboard.views.index'),
    url(r'^count/$', 'hyperion.dashboard.views.count'),
)
