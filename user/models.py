from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TodoUser(models.Model):
	name= models.CharField(max_length=40)
	email=models.EmailField()
	user=models.OneToOneField(User,on_delete=models.CASCADE)


	def __str__(self):
		return ' {} '.format(self.name)

