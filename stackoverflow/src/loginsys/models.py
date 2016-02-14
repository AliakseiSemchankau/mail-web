from django.db import models
from django.contrib.auth.models import User, UserManager, AbstractBaseUser
import os
# Create your models here.

def get_image_path(instance, filename):
    return os.path.join('users', str(instance.user.id), 'ava.jpg')

class UserProfile(models.Model):

    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    avatar = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

