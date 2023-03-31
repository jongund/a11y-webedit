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

from django.core.exceptions      import ObjectDoesNotExist
from django.core.exceptions      import ImproperlyConfigured
from django.contrib.sites.models import Site
from django.contrib.auth.models  import User
from accounts.models             import Profile

def create_profiles():

  for user in User.objects.all():

    try:
      profile = user.profile
      print("User has profile: " + profile.user.username + " (" + profile.slug + ")")

    except ObjectDoesNotExist:
      print("Create Profile: " + user.username)
      profile = Profile(user=user)
      profile.save()

create_profiles()
