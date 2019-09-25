from django.db import models

from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, AbstractUser, PermissionsMixin, BaseUserManager


class ExtendedUser(AbstractUser):
    phone = models.CharField(max_length=12)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.id}: {self.username}'


class Profile(models.Model):
    user = models.OneToOneField(ExtendedUser, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)
    address = models.CharField(max_length=300)
    address2 = models.CharField(max_length=300)
    registration_date = models.DateTimeField(auto_now_add=True)


class Project(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=1000)
    creator = models.ForeignKey(ExtendedUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Block(models.Model):
    name = models.CharField(max_length=300)
    type = models.IntegerField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Task(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=1000)
    creator = models.ForeignKey(ExtendedUser, on_delete=models.CASCADE)
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class TaskDocument(models.Model):
    file = models.FileField()
    creator = models.ForeignKey(ExtendedUser, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class TaskComment(models.Model):
    body = models.TextField(max_length=1000)
    creator = models.ForeignKey(ExtendedUser, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


# Create your models here.
