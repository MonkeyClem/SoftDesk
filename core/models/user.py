from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.exceptions import ValidationError

# Create your models here.

""" I chose to keep this function in order to keep global safety, outside the use of DRF (e.g : 
if we want to create a user via shell)"""
def validate_age(value : int) : 
    if value < 15 : 
        raise ValidationError(
            f'You must be at least 15 years old to register... Sorry :( )'
        )
    
class CustomUserManager(BaseUserManager): 
    def create_user(self, username, email, password= None, age=None, **extra_fields): 
        if age is None or age < 15 : 
            raise ValidationError("You must be at least 15 years old to register... Sorry :( ")
        email = self.normalize_email(email)
        user = self.model(username=username, email = email, age=age, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        pass 

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, age=99, **extra_fields)
    
class User(AbstractUser) : 
    age = models.PositiveIntegerField(validators=[validate_age])
    can_be_contacted = models.BooleanField(default=False)
    accept_to_share_data = models.BooleanField(default=False)

    objects = CustomUserManager()

    def __repr__(self):
        return self.username