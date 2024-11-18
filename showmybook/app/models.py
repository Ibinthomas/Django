from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class movie(models.Model):
    movie_name=models.TextField()
    back_img=models.FileField()
    for_img=models.FileField()
    time=models.TextField()
    category=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.movie_name


class lang(models.Model):
    language=models.TextField()

class movie_lang(models.Model):
    movie=models.ForeignKey(movie,on_delete=models.CASCADE)
    lang=models.ForeignKey(lang,on_delete=models.CASCADE)
    
    
class members(models.Model):
    name=models.TextField()
    img=models.FileField()
    position=models.TextField()
    cast=models.BooleanField(default=False)
    craw=models.BooleanField(default=False)
    movie=models.ForeignKey(movie,on_delete=models.CASCADE)
