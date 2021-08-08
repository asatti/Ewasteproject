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