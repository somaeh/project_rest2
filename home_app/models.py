from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .mangers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    full_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'phone_number'         # این فیلدی هست که براساس آن کاربر را اعتبار سنجی می کنید
    REQUIRED_FIELDS = ['email', 'full_name']    #در قسمت سوپر یوزیر چه فیلدهایی پرسیده شود برای ورود
    
    
    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
    @property
    def is_staff(self):
        return self.is_admin

class Person(models.Model):
    name =  models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    email = models.EmailField()
    
    
    def __str__(self):
        return self.name
