from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import UserManager
from django.utils import timezone

# Create your models here.
class CustomUserManager(UserManager):
    def _create_user(self,email,password,**extra_fields):
        if not email:
            raise("email is not provided")
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
    def create_user(self, email,password,**extra_fields):
        extra_fields.setdefault("is_staff",False)
        extra_fields.setdefault("is_superuser",False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email,password,**extra_fields):
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)
        return self._create_user(email, password, **extra_fields)
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(max_length=225)
    
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    date_joined = models.DateTimeField(timezone.now,null=True,default=None)
    last_login = models.DateTimeField(timezone.now,null=True,default=None)
    
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS=[]
    
    class Meta:
        verbose_name = 'User'
        
 
class Candidate(models.Model):
    student_id = models.AutoField(primary_key=True)
    login = models.ForeignKey(CustomUser,on_delete=models.PROTECT)
    email = models.EmailField(null=True, unique=False,default=None)
    firstname = models.CharField(max_length=127)
    lastname = models.CharField(max_length=127)
    gender = models.CharField(max_length=15)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=15)
    state = models.CharField(max_length=127)
    dob = models.DateField()
    student_class = models.IntegerField(default=0)
