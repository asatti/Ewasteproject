from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
#user manager

class CustomUser(AbstractUser):
	email = models.EmailField(_('email address'), unique=True)
	first_name = models.CharField(max_length=150, blank=True)
	last_name = models.CharField(max_length=150, blank=True)
	start_date = models.DateTimeField(default=timezone.now)
	address = models.CharField(max_length=300, unique=True) 
	is_active = models.BooleanField(default=False)
	@property
	def user_name(self):
		return self.first_name + " " + self.last_name
	
class Item(models.Model):
	WEIGHT_CHOICES = (
		("1-10", "1lbs - 10lbs"),
		("11-20", "11lbs - 20lbs"),
		("21-30","21lbs - 30lbs") ,#add pounds
		("31-40","31lbs - 40lbs"),
		("41-50","41lbs - 50lbs"),
		("51-60","51lbs - 60lbs"),
		("61-70","61lbs - 70lbs"),
		("71-80","71lbs - 80lbs"),
		("81-90","81lbs - 90lbs"),
		("91-100","91lbs - 100lbs")
	)
	estimated_weight_in_pounds = models.CharField(
		max_length = 20,
		choices = WEIGHT_CHOICES,
		default = "1-10"
	)
	OBJECT_TYPE_CHOICES = (
		("battery", "battery"),
		("none" , "none"),
		("monitor" , "monitor"), #think of more later
	)
	object_type = models.CharField(
		max_length = 20,
		choices = OBJECT_TYPE_CHOICES,
		default = "none"
	)
	is_delivered = models.BooleanField(default=False)
class Driver(models.Model): #look up
	email = models.EmailField(_('email address'), unique=True)
	first_name = models.CharField(max_length=150, blank=True)
	last_name = models.CharField(max_length=150, blank=True)
	start_date = models.DateTimeField(default=timezone.now)
	address = models.CharField(max_length=300, unique=True) #change "char field"
	is_active = models.BooleanField(default=False)

	@property
	def user_name(self):
		return self.first_name + " " + self.last_name

	start_time = models.DateTimeField()
	end_time = models.DateTimeField()