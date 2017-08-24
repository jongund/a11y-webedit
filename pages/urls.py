from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.new, name = 'new'),
	url(r'^(?P<slug>[-\w]+)/output/$', views.run, name = 'run'),
	url(r'^(?P<slug>[-\w]+)/delete/$', views.delete, name = 'delete'),
	url(r'^(?P<slug>[-\w]+)/copy/$', views.copy, name = 'copy'),
	url(r'^all/$', views.show_all, name='show_all'),
	url(r'^(?P<slug>[-\w]+)/$', views.show, name = 'show'),
	#url(r'^(?P<slug>[-\w]+)/output$', views.run),
]

#target = "_user.id"

