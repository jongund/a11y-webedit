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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
#	url(r'^$', lambda r: HttpResponseRedirect('pages/new')),
	url(r'^', include('pages.urls')),
    url(r'^accounts/', include('django_registration.backends.activation.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    # url(r'^accounts/password_reset/', auth_views.PasswordChangeView.as_view()),
    # url(r'^accounts/password_reset/done', auth_views.PasswordChangeDoneView.as_view()),
    # url(r'^reset/',    include('password_reset.urls')),
    url(r'^profile/',  include('accounts.urls')),

    # url(r'^login$', auth_views.LoginView, name='login'),
#    url(r'^login/$',                ShibbolethLogin.as_view(),       name='shib_login'),
#    url(r'^logout/$',               ShibbolethLogout.as_view(),      name='shib_logout'),
#    url(r'^discovery/$',            ShibbolethDiscovery.as_view(),   name='shib_discovery'),
#    url(r'^inst/(?P<domain>\w+)/$', ShibbolethInstitution.as_view(), name='shib_institution'),
#    url(r'^header-info/$',          HeaderInfo.as_view(),            name='shib_header_info'), # debug information

]

