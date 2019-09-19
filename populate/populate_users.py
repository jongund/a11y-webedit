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

users = (
    (settings.ADMIN_USERNAME, settings.ADMIN_PASSWORD, settings.ADMIN_EMAIL, settings.ADMIN_FIRST_NAME,
     settings.ADMIN_LAST_NAME, True, True),
)


def create_users(users):
    for person in users:

        try:
            print("Update User: " + person[0])
            user = User.objects.get(username=person[0])
            user.email = person[2]
            user.first = person[3]
            user.last = person[4]
            user.is_superuser = person[5]
            user.is_staff = person[6]
            user.set_password(person[1])


        except ObjectDoesNotExist:
            print("Create User: " + person[0])
            user = User(username=person[0], email=person[2], first_name=person[3], last_name=person[4], is_superuser=person[5],
                        is_staff=person[6])
            user.set_password(person[1])

        user.save()


def set_site(name, url):
    site = Site.objects.get_current()
    site.domain = url
    site.name = name
    site.save()


create_users(users)
set_site(settings.SITE_NAME, settings.SITE_URL)
