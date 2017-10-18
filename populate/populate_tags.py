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

from django.core.exceptions 	import ObjectDoesNotExist
from pages.models import Tag


def create_tag(tag):

	try:
		print("Update Tag: " + tag.slug),
		t = Tag.objects.get(slug=tag.slug)

		t.title       = tag.title
		t.description = tag.description

	except ObjectDoesNotExist:
		print("Create Tag: " + tag.slug)
		t = Tag(slug= tag.slug, title=tag.title, description=tag.description)

	t.save()

tag = type("myobj",(object,),dict(slug='', title='', description=''))
tag.slug = 'structure'
tag.title = 'Structure'
tag.description = 'Problems and solutions related ARIA landmarks, headings, page titles and navigation.'

create_tag(tag)

tag.slug = 'links'
tag.title = 'Links'
tag.description = 'Examples related to HTML links.'

create_tag(tag)

tag.slug = 'controls'
tag.title = 'Form Controls'
tag.description = 'Examples related to HTML form controls.'

create_tag(tag)
