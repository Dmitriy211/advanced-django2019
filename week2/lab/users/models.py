from django.db import models

from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, AbstractUser, PermissionsMixin, BaseUserManager


class Profile(models.Model):
    bio = models.TextField(max_length=500)
    address = models.CharField(max_length=300)
    address2 = models.CharField(max_length=300)
    registration_date = models.DateTimeField(auto_now_add=True)


class ExtendedUser(AbstractUser):
    phone = models.CharField(max_length=12)
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.id}: {self.username}'


# Create your models here.
