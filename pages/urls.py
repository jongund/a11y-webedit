from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^new/$', views.new,      name = 'new'),

  url(r'^user/(?P<username>\w+)/all/$',                     views.show_all, name = 'show_all'),
  url(r'^user/(?P<username>\w+)/(?P<slug>[-\w]+)/$',        views.show,     name = 'show'),
	url(r'^user/(?P<username>\w+)/(?P<slug>[-\w]+)/output/$', views.run,      name = 'run'),
	url(r'^user/(?P<username>\w+)/(?P<slug>[-\w]+)/delete/$', views.delete,   name = 'delete'),
	url(r'^user/(?P<username>\w+)/(?P<slug>[-\w]+)/copy/$',   views.copy,     name = 'copy'),

	url(r'^guest/(?P<slug>[-\w]+)/$',                        views.show_anon, name = 'show_anon'),
	url(r'^guest/output/(?P<slug>[-\w]+)/$',                 views.run_anon,  name = 'run_anon'),
  url(r'^guest/copy/(?P<username>\w+)/(?P<slug>[-\w]+)/$', views.copy_anon, name = 'copy_anon'),

	url(r'^samples/$', views.show_samples, name='show_samples')
]

