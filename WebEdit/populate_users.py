import django 
import json

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
			
		except ObjectDoesNotExist:
			print("Create User: " + person[0])
			user = User(username=person[0], is_superuser=person[2], is_staff=person[3])
			
		user.save()
		
create_users(users)