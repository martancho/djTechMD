from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User,unique=True, null=False, db_index=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

class Contact(models.Model):
	project_name = models.CharField(max_length=200, null=True)
	client_name = models.CharField(max_length=200, blank=True, null=True)
	client_address = models.CharField(max_length=200, blank=True, null=True)
	client_address2 = models.CharField(max_length=200, blank=True, null=True)
	phone_number = models.CharField(max_length=200, null=True)
	client = models.CharField(max_length=250, null=True)
	today_date = models.DateTimeField(auto_now_add=True, auto_now=False)
	rfi = models.CharField(max_length=7, null=True)
	email = models.EmailField(max_length=254, null=True)
	user = models.CharField(max_length=200, null = True)
	info_requested = models.TextField(max_length=250, null=True)
	description = models.TextField(max_length=500, null=True)
	response = models.TextField(max_length=500, null=True)
	user_signature = models.CharField(max_length=200, null=True)
	client_signature = models.CharField(max_length=200, null=True)
	user_date = models.DateTimeField(default=timezone.now)
	client_date = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.client_name 



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()