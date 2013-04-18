from django.conf.urls import patterns, url

from events import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<event_id>\d+)/$', views.detail, name='detail'),
    url(r'^create', views.create, name='create'),
	url(r'^list', views.list, name='list'),
)
