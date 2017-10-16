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
	title = models.CharField(max_length=128)
	description = models.CharField(max_length=200,blank=True)
	webKey = models.CharField(max_length=32) #SHOULD JUST BE UNIQUE FOR ONE USER
	#=>letters and numbers excluding one and l
	public = models.BooleanField(default=True)
	lastUpdated = models.DateTimeField(auto_now=True)

	#-----------ADMIN----------------
	sample = models.BooleanField(default=False)
	tags = models.ManyToManyField('Tag', related_name='pages', blank=True)

	#----------EDITOR TEXT-----------
	htmlHead = models.TextField(blank=True)
	htmlBody = models.TextField(blank=True)
	css = models.TextField(blank=True)
	javascript = models.TextField(blank=True)

	class Meta:
		ordering = ['title']
		unique_together = ('user', 'webKey')


class Tag(models.Model):
	def __str__(self):
		return self.title;
	title=models.CharField(max_length=20)
	description=models.CharField(max_length=50,blank=True,null=True)
	slug=models.CharField(max_length=32,unique=True,default='')


