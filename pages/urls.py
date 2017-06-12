from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^new/$', views.new, name = 'new'),
	url(r'^(?P<slug>[-\w]+)/output/$', views.run),
	url(r'^all/$', views.show_all, name='show_all'),
	url(r'^(?P<slug>[-\w]+)/$', views.show),
	#url(r'^(?P<slug>[-\w]+)/output$', views.run),
]

#target = "_user.id"

