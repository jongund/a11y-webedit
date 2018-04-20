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

from django.utils.crypto import get_random_string

from pages.models                import Page

def init_page_slugs():

  for page in Page.objects.all():

    if len(page.slug) == 0 and len(page.webKey) > 0:
      for c in page.webKey.lower():
        if 'abcdefghijklmnopqrstuvwxyz1234567890_-'.find(c) >= 0:
          page.slug += c
        else:
          if '.'.find(c) >= 0:
            page.slug += '-'

    if len(page.slug) == 0:
      page.slug = get_random_string(length=6)

    print('[webKey]: ' + page.webKey)
    print('  [slug]: ' + page.slug)

    page.save()

init_page_slugs()
