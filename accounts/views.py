from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import auth

from WebEdit.settings import SITE_URL
from WebEdit.settings import SHIBBOLETH_URL
from WebEdit.settings import SHIBBOLETH_AUTH
from WebEdit.settings import ADMIN_USERNAME

from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView
from django.views.generic import FormView
from django.views.generic import CreateView
from django.views.generic import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import EditProfileForm, ProfileForm
from .models import Profile
from django.contrib.auth.models import User

# Create your views here.

def show_profile(request):
    u = request.user

    profile = Profile.objects.get(user=request.user)
    userAccount = User.objects.get(profile__user=request.user)

    if request.method == "POST":

        form = EditProfileForm(data=request.POST or None, instance=userAccount)
        profile_form = ProfileForm(data=request.POST or None, instance=profile)

        if form.is_valid():
            form.save()
            profile_form.save()
            return redirect(reverse('show_profile'))

    else:
        form = EditProfileForm(instance=userAccount)
        profile_form = ProfileForm(instance=profile)

    context = {
        'u': u,
        'form': form,
        'profileForm': profile_form
    }
    return render(request, "accounts/profile.html", context)



class ShibbolethInfo(LoginRequiredMixin, TemplateView):
    template_name = 'registration/header_info.html'


class ShibbolethLogout(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        auth.logout(self.request)
        self.url = SITE_URL + '/Shibboleth.sso/Logout'
        return super(ShibbolethLogout, self).get_redirect_url(*args, **kwargs)


class ShibbolethUpdate(RedirectView):

    def get_redirect_url(self, *args, **kwargs):

        user = self.request.user

        if user.username == ADMIN_USERNAME:
            user.is_staff = True
            user.is_superuser = True
            user.save()

        # Try to populate user information from shibboleth header information
        if not user.is_anonymous and user.first_name == '':
            try:
                user.first_name = self.request.META['givenName']
                user.save()
            except:
                pass

        if not user.is_anonymous and user.last_name == '':
            try:
                user.last_name = self.request.META['sn']
                user.save()
            except:
                pass

        if not user.is_anonymous and user.email == '':
            try:
                user.email = self.request.META['mail']
                user.save()
            except:
                try:
                    if user.username.find('@') > 0 and user.username.find('.'):
                        user.email = user.username
                        user.save()
                except:
                    pass

        self.url = SITE_URL

        return super(ShibbolethUpdate, self).get_redirect_url(*args, **kwargs)


class ShibbolethLogin(RedirectView):

    def get_redirect_url(self, *args, **kwargs):

        login_url = 'https://webedit-dev.disability.illinois.edu/update'

        self.url = SHIBBOLETH_URL + '?entityID=' + SHIBBOLETH_AUTH + '&amp;target=' + login_url

        return super(ShibbolethLogin, self).get_redirect_url(*args, **kwargs)
