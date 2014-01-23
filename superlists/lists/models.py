from django.db import models

class List(models.Model):
	pass

# Create your models here.
class Item(models.Model):
	text = models.TextField()
	list = models.ForeignKey(List)