from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Page(models.Model):
	def __str__(self):
		return "\nTitle: "+self.title+"\nDescription:\n"+self.description
		
	#page_id = unique id...
	
	users = models.ManyToManyField(User,
		related_name="pages")
	
	title = models.CharField(max_length=30)
	description = models.CharField(max_length=200)
	htmlHead = models.TextField()
	htmlBody = models.TextField()
	css = models.TextField()
	javascript = models.TextField()
	lastUpdated = models.DateField(auto_now=True)
	
	