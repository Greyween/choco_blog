from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	photo = models.ImageField(blank=True, upload_to='profile_images')
	karma = models.IntegerField(default=0)

	user = models.OneToOneField(User)

	def __str__(self):
		return self.user.username