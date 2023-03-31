from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^profile/$', views.show_profile, name = 'show_profile'),
]


