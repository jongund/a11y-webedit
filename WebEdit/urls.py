"""WebEdit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

import django.contrib.auth.urls
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import views as auth_views

from accounts.views import ShibbolethLogin
from accounts.views import ShibbolethLogout
from accounts.views import ShibbolethDiscovery
from accounts.views import ShibbolethInstitution
from accounts.views import HeaderInfo

from WebEdit.settings import SHIBBOLETH_ENABLED

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('pages.urls')),
    url(r'^profile/',  include('accounts.urls')),
]

if SHIBBOLETH_ENABLED:
    urlpatterns += [
        url(r'^login/$', ShibbolethLogin.as_view(), name='login'),
        url(r'^logout/$', ShibbolethLogout.as_view(), name='logout'),
        url(r'^inst/$', ShibbolethInstitution.as_view(), name='shib_login'),
        url(r'^header-info/$', HeaderInfo.as_view(), name='header_info'),  # debug information
    ]
else:
    urlpatterns += [
        url(r'^accounts/', include('django_registration.backends.activation.urls')),
        url(r'^accounts/', include('django.contrib.auth.urls')),
    ]

