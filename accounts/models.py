from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.manager import CustomUserManager
# Create your models here.


class User(AbstractUser):
    email = models.CharField(max_length=100, unique=True)
    mobile_number = models.CharField(max_length=15, db_index=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.IntegerField(blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email