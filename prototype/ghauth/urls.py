from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'ghauth.views.home', name='home'),
    url(r'^done$', 'ghauth.views.done', name='done'),
    # Examples:
    # url(r'^ghpr/', include('ghpr.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
