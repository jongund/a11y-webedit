from django.db import models

# Create your models here.

class Page(models.Model):
	#page_id = unique id...
	title = models.CharField(max_length=30)
	description = models.CharField(max_length=200)
	htmlHead = models.TextField()
	htmlBody = models.TextField()
	css = models.TextField()
	javascript = models.TextField()
	lastUpdated = models.DateField(auto_now=True)
	
	