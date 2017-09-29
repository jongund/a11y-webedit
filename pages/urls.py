from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^new/$', views.new, name = 'new'),
	url(r'^(?P<username>\w+)/output/(?P<slug>[-\w]+)/$', views.run, name = 'run'),
	url(r'^(?P<username>\w+)/delete/(?P<slug>[-\w]+)/$', views.delete, name = 'delete'),
	url(r'^(?P<username>\w+)/copy/(?P<slug>[-\w]+)/copy/$', views.copy, name = 'copy'),
	url(r'^all/$', views.show_all, name='show_all'),
	url(r'^(?P<username>\w+)/(?P<slug>[-\w]+)/$', views.show, name = 'show'),
]

