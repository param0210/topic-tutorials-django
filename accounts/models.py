from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.
GENDER=(
    ('male','MALE'),
    ('female','FEMALE'),
    ('transgender','TRANSGENDER')
    )

class MyUser(AbstractUser):
    first_name=models.CharField(max_length=100,null=False,blank=False)
    last_name=models.CharField(max_length=100,null=True,blank=True)
    gender=models.CharField(max_length=100,choices=GENDER,null=True,blank=True)
    mobile_number=models.CharField(max_length=100,null=True,blank=True)
    date_of_birth=models.DateField(null=True,blank=True)
    age=models.PositiveIntegerField(null=True)
    image=models.ImageField(upload_to='profile',null=True,blank=True)

    def __str__(self):
        return self.username


class Page(models.Model):
    user=models.OneToOneField(MyUser,on_delete=models.CASCADE,primary_key=True)
    page_name=models.CharField(max_length=100,null=False,blank=False)
    pub_date=models.DateField(null=True,blank=True)


    def __str__(self):
        return self.page_name


class Song(models.Model):
    user=models.ManyToManyField(MyUser)
    song_title=models.CharField(max_length=100,null=False,blank=False)
    duration=models.TimeField(null=True,blank=True)

    def __str__(self):
        return self.song_title