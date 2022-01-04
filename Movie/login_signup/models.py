from django.db import models
from django.db import models

from django.contrib.auth.models import Permission, User
from django.contrib.auth.models import AbstractUser

from datetime import datetime, timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class User(AbstractUser):
    is_client = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True, default='uploads/img_avatar.png')
    expiration_date = models.DateTimeField(default=datetime.now() + timedelta(days=1))

    def count_rated_movies(self):
        count = self.client_user.all().count()
        return count

@receiver(post_save, sender=User) 
def user_post_save_receiver(sender, instance, created, *args, **kwargs): 
    """
    after saved in the database
    """
    if created:
        if instance.email == '':
            instance.is_active = True
            instance.is_verified = True
            instance.save()

