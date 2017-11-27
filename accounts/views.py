from django.shortcuts import render
from django.http import HttpResponse

from WebEdit.settings import SITE_URL
from WebEdit.settings import SHIB_URL
from WebEdit.settings import ADMIN_USERNAME

from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic          import TemplateView
from django.views.generic          import FormView
from django.views.generic          import CreateView
from django.views.generic          import RedirectView
from django.contrib.auth.mixins    import LoginRequiredMixin


# Create your views here.

def show_profile(request):
	u = request.user
	context = {
		'u' : u,
		}
	return render(request, "accounts/profile.html", context)

class HeaderInfo(LoginRequiredMixin, TemplateView):
   template_name = 'registration/header_info.html'


class ShibbolethLogout(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        self.url = SITE_URL + '/Shibboleth.sso/Logout'
        return super(ShibbolethLogout, self).get_redirect_url(*args, **kwargs)


class ShibbolethLogin(RedirectView):

    def get_redirect_url(self, *args, **kwargs):

        user = self.request.user

        if user.username == ADMIN_USERNAME:
            user.is_staff     = True
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
                user.last_name  = self.request.META['sn']
                user.save()
            except:
                pass

        if not user.is_anonymous and user.email == '':
            try:
                user.email      = self.request.META['mail']
                user.save()
            except:
                try:
                    if user.username.find('@') > 0 and user.username.find('.'):
                        user.email = user.username
                        user.save()
                except:
                    pass

        self.url = SITE_URL

        return super(ShibbolethLogin, self).get_redirect_url(*args, **kwargs)

class ShibbolethDiscovery(TemplateView):
    template_name = 'shib_discovery.html'

class ShibbolethInstitution(RedirectView):
    def get_redirect_url(self, *args, **kwargs):

        self.url = SHIB_URL

        try:
            ip = InstitutionalProfile.objects.get(domain=kwargs['domain'])
            self.url += '/Shibboleth.sso/Login?entityID=' + ip.authentication + '&target=' + SITE_URL
        except:
            try:
                ip =  InstitutionalProfile.objects.get(alt_domain=kwargs['domain'])
                self.url += '/Shibboleth.sso/Login?entityID=' + ip.authentication + '&target=' + SITE_URL
            except:
                ip =  None

        return super(ShibbolethInstitution, self).get_redirect_url(*args, **kwargs)

