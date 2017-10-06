from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^all/$', views.show_all_samples, name='show_all_samples'),
]

