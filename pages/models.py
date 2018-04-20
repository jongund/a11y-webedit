from datetime import datetime

from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

class Page(models.Model):

	#------------USER----------------
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
	related_name = "pages", blank=True, null=True)
	#potentially add more models for sharing

	#----------SETTINGS--------------
	title       = models.CharField(max_length=128)
	description = models.CharField(max_length=512,blank=True)
	webKey      = models.CharField(max_length=32,blank=True,default="")
	slug        = models.SlugField(max_length=32,default="")
	#=>USER letters and numbers excluding one and l

	public = models.BooleanField(default=True)

	created     = models.DateTimeField(auto_now_add=False, default=datetime.now)
	lastUpdated = models.DateTimeField(auto_now=True)
	save_count  = models.IntegerField(default=0)

	#-----------ADMIN----------------
	sample     = models.BooleanField(default=False)
	assignment = models.BooleanField(default=False)
	tags       = models.ManyToManyField('Tag', related_name='pages', null=True, blank=True)

	#----------EDITOR TEXT-----------
	htmlHead   = models.TextField(blank=True)
	htmlBody   = models.TextField(blank=True)
	css        = models.TextField(blank=True)
	javascript = models.TextField(blank=True)

	class Meta:
		ordering = ['-lastUpdated', 'title']
		unique_together = ('user', 'slug')

	def __str__(self):
		return self.title + ' (' + str(self.user) + ')'

	def save(self):
			self.save_count += 1  # Keep track of how many times someone saves a page
			self.lastUpdated = datetime.now()
			super(Page, self).save()  # Call real save

class Tag(models.Model):

	title       = models.CharField(max_length=128)
	description = models.CharField(max_length=512,blank=True,null=True)
	slug        = models.CharField(max_length=32,unique=True,default='')

	def __str__(self):
		return self.title;

	def get_public_count(self):
		return self.pages.filter(public=True).count()

	def get_public(self):
		return self.pages.filter(public=True)


