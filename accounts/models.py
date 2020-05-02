from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	fullname = models.CharField(max_length=30)
	bio = models.TextField()

	def __str__(self):
		return f"{self.user.username} Profile"