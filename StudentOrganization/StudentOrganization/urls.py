from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('main.urls')),
    url(r'^main/', include('main.urls')),
    url(r'^events/', include('events.urls', namespace="events")),
    url(r'^users/', include('users.urls', namespace="users")),
    url(r'^admin/', include(admin.site.urls)),
)
