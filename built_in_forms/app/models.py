from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class project_user(models.Model):
    name=models.TextField()
    age=models.IntegerField()
    email=models.EmailField()
    place=models.TextField()
    