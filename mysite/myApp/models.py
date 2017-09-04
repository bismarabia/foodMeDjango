from django.db import models
from myApp.utils import Timestampable

class User(Timestampable, models.Model):
	idd 		= models.IntegerField(default=0)
	username 	= models.CharField(max_length=256, null=True)	
	password 	= models.CharField(max_length=256, null=True)
	credit 		= models.FloatField(default=0.0)
	def __str__(self):
		return self.username

class LoginLog(Timestampable, models.Model):
	username = models.CharField(max_length=256, null=True)	
	password = models.CharField(max_length=256, null=True)
	def __str__(self):
		return self.username

class FoodList(Timestampable, models.Model):
	pic_id 	= models.IntegerField(default=0)
	name 	= models.CharField(max_length=256)
	price	= models.FloatField(default=0.0)
	def __str__(self):
		return self.name

class PurchaseLog(Timestampable, models.Model):
	user 		= models.ForeignKey(User, related_name='user_purchase_log')
	name 		= models.CharField(max_length	= 256)
	quantity	= models.IntegerField(default	= 1)
	price		= models.FloatField(default 	= 0.0)
	time 		= models.DateTimeField(blank	= True)
	def __str__(self):
		return self.name
		