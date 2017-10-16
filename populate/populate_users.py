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
from django.contrib.auth.models import User

users = (
	(settings.ADMIN_USERNAME, settings.ADMIN_PASSWORD, True, True),
)

def create_users(users):

	for person in users:

		try:
			print("Update User: " + person[0]),
			user = User.objects.get(username=person[0])
			user.is_superuser = person[2]
			user.is_staff 	  = person[3]
			user.set_password(person[1])

		except ObjectDoesNotExist:
			print("Create User: " + person[0])
			user = User(username=person[0], is_superuser=person[2], is_staff=person[3])
			user.set_password(person[1])
			
		user.save()

create_users(users)
