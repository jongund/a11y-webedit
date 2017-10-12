from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^new/$', views.new, name = 'new'),
	url(r'^user/(?P<username>\w+)/output/(?P<slug>[-\w]+)/$', views.run, name = 'run'),
	url(r'^user/(?P<username>\w+)/delete/(?P<slug>[-\w]+)/$', views.delete, name = 'delete'),
	url(r'^user/(?P<username>\w+)/copy/(?P<slug>[-\w]+)/$', views.copy, name = 'copy'),
	url(r'^all/$', views.show_all, name='show_all'),
	url(r'^user/(?P<username>\w+)/(?P<slug>[-\w]+)/$', views.show, name = 'show'),
	url(r'^guest/(?P<slug>[-\w]+)/$', views.show_anon, name = 'show_anon'),
	url(r'^guest/output/(?P<slug>[-\w]+)/$', views.run_anon, name = 'run_anon'),
	url(r'^samples/$', views.show_samples, name='show_samples')
]

