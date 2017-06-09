from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^new/$', views.new, name = 'new'),
	url(r'^output/$', views.run, name='run'),
	url(r'^all/$', views.show_all, name='show_all'),
	url(r'^(?P<slug>[-\w]+)/$', views.show),
]

#target = "_user.id"

