import django
import json
import sys
import os

fp = os.path.realpath(__file__)
path, filename = os.path.split(fp)
webedit_path = os.path.split(path)[0]

sys.path.append(webedit_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WebEdit.settings")

from django.conf import settings

django.setup()

from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ImproperlyConfigured
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from accounts.models import Profile
from django.urls import reverse

from WebEdit.settings import SITE_URL
from WebEdit.settings import SHIBBOLETH_URL
from WebEdit.settings import SHIBBOLETH_AUTH
from WebEdit.settings import ADMIN_USERNAME

for s in Site.objects.all():
  print("\nSite: " + s.domain + " " + s.name)

print("\n       SITE URL: " + SITE_URL)
print("\n SHIBBOLETH URL: " + SHIBBOLETH_URL)
print("\nSHIBBOLETH AUTH: " + SHIBBOLETH_AUTH)
print("\nshib_update URL: " + SITE_URL + reverse('shib_update'))

for u in User.objects.all():
  print( "\nUsername: " +  u.username)
  print( "Staff: "      + str(u.is_staff))
  print( "Superuser: "      + str(u.is_superuser))

  try:
    print( "Profile: " +  str(u.profile))
  except:
    print( "no profile")

  if u.username == 'jongund@illinois.edu':
    u.is_staff = True
    u.is_superuser = True
    u.save()
