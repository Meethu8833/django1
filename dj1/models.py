from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# class CustomUser(AbstractUser):
#     phone_number=models.CharField(max_length=100,null=True)
#     address=models.CharField(max_length=100,null=True)

class CustomUser(AbstractUser):
    date_of_birth=models.DateField(null=True)
    profile_picture=models.ImageField(null=True,upload_to='image/')

class Author(models.Model):
    name=models.CharField(max_length=100)
    bio=models.CharField(max_length=100)
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=200)
    image=models.ImageField(upload_to='image/')
    published_date=models.DateField()
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
