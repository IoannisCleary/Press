from django.db import models
import django_filters
# Create your models here.

class Feed(models.Model):
	subject = models.CharField(max_length = 128, unique = True)
	link = models.URLField()
	def __unicode__(self): 
		return self.subject

class Item(models.Model):
	feed = models.ForeignKey(Feed)
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length = 256, unique=True)
	link = models.URLField()
	description = models.CharField(max_length = 2000)
	dateTime = models.CharField(max_length = 20, default="00:00 00/00/0000")
	def __unicode__(self): 
		return self.title
	class Meta:
		verbose_name_plural = "Items"
		