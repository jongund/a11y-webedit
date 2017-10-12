from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
#from django.utils.crypto import get_random_string

class Page(models.Model):

	def __str__(self):
		return "Title: \""+self.title+"\", Description: \""+self.description+\
			"\", Username: \""+self.user.username+"\""
			
	#------------USER----------------
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, 
	related_name = "page", blank=True, null=True)
	#potentially add more models for sharing
	
	#----------SETTINGS--------------
	title = models.CharField(max_length=30)
	description = models.CharField(max_length=200,blank=True)
	web_key = models.CharField(max_length=32) #SHOULD JUST BE UNIQUE FOR ONE USER
	#=>letters and numbers excluding one and l
	public = models.BooleanField(default=True)
	sample = models.BooleanField(default=False)
	lastUpdated = models.DateTimeField(auto_now=True)
	
	#----------EDITOR TEXT-----------
	htmlHead = models.TextField(blank=True)
	htmlBody = models.TextField(blank=True)
	css = models.TextField(blank=True)
	javascript = models.TextField(blank=True)
	
	class Meta:
		unique_together = ('user', 'web_key')
	
	