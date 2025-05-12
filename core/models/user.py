from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser

from django.core.exceptions import ValidationError

# Create your models here.

""" I chose to keep this function in order to keep global safety, outside the use of DRF (e.g : 
if we want to create a user via shell)"""
def validate_age(value : int) : 
    if value < 15 : 
        raise ValidationError(
            f'You must be at least 15 years old to register... Sorry :( )'
        )
    
class User(AbstractUser) : 
    age = models.PositiveIntegerField(validators=[validate_age])
    can_be_contacted = models.BooleanField(default=False)
    accept_to_share_data = models.BooleanField(default=False)

    def __repr__(self):
        return self.username