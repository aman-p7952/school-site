from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager

# Create your models here.
class Login(AbstractBaseUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(max_length=225)
    objects = UserManager()
class User(models.Model):
    login = models.OneToOneField(Login,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=127)
    lastname = models.CharField(max_length=127) 
    gender = models.CharField(max_length=15)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=15)
    state = models.CharField(max_length=127)
    dob = models.DateField()
  


  