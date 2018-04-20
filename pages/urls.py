from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.new,      name = 'new'),

  url(r'^user/(?P<profile_slug>\w+)/all/$',                     views.show_all, name = 'show_all'),
  url(r'^user/(?P<profile_slug>\w+)/(?P<page_slug>[-\w]+)/$',        views.show,     name = 'show'),
	url(r'^user/(?P<profile_slug>\w+)/(?P<page_slug>[-\w]+)/output/$', views.run,      name = 'run'),
	url(r'^user/(?P<profile_slug>\w+)/(?P<page_slug>[-\w]+)/delete/$', views.delete,   name = 'delete'),
	url(r'^user/(?P<profile_slug>\w+)/(?P<page_slug>[-\w]+)/copy/$',   views.copy,     name = 'copy'),

	url(r'^guest/(?P<page_slug>[-\w]+)/$',                        views.show_anon, name = 'show_anon'),
	url(r'^guest/(?P<page_slug>[-\w]+)/output/$',                 views.run_anon,  name = 'run_anon'),
  url(r'^guest/(?P<page_slug>[-\w]+)/copy/$', views.copy_anon, name = 'copy_anon'),

	url(r'^samples/$', views.show_samples, name='show_samples')
]

