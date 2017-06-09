from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string

class Page(models.Model):

	def __str__(self):
		return "Title: \""+self.title+"\", Description: \""+self.description+\
			"\", Username: \""+self.user.username+"\""
	
	#------------USER----------------
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name = "page",
		blank=True)
	#potentially add more models for sharing
	
	#----------SETTINGS--------------
	title = models.CharField(max_length=30)
	description = models.CharField(max_length=200)
	web_key = models.CharField(max_length=6,default=get_random_string(length=6).lower(),unique=True)
	#=>letters and numbers excluding one, el
	#=>all letters lowercase
	public = models.BooleanField(default=True)
	lastUpdated = models.DateTimeField(auto_now=True)
	
	#----------EDITOR TEXT-----------
	htmlHead = models.TextField()
	htmlBody = models.TextField()
	css = models.TextField()
	javascript = models.TextField()
	
	