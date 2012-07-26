from django.conf.urls.defaults import patterns, url, include
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hyperion.views.home', name='home'),
    # url(r'^hyperion/', include('hyperion.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'', include('hyperion.dashboard.urls')),
)
