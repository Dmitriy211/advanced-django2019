from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, AbstractUser, PermissionsMixin, BaseUserManager
from .constants import TASK_STATUSES, TASK_TODO, TASK_DONE, TASK_DOING
from .utils.upload import task_document_path
from .utils.validators import validate_extension, validate_file_size
import os
import transliterate


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

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name

    @property
    def tasks_count(self):
        return self.task_set.count()


class ProjectMember(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="members")
    user = models.ForeignKey(ExtendedUser, on_delete=models.CASCADE, related_name="memberships")



class TaskManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().all()

    def done_tasks(self):
        return self.filter(status=TASK_DONE)

    def doing_tasks(self):
        return self.filter(status=TASK_DOING)

    def todo_tasks(self):
        return self.filter(status=TASK_TODO)

    def filter_by_status(self, status):
        return self.filter(status=status)


class Task(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=1000)
    creator = models.ForeignKey(ExtendedUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(choices=TASK_STATUSES, default=TASK_TODO)
    # block = models.ForeignKey(Block, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    class Meta:
        unique_together = ('project', 'name')
        ordering = ('name', 'status',)

    def __str__(self):
        return self.name


class TaskDocument(models.Model):
    file = models.FileField(upload_to=task_document_path,
                            validators=[validate_file_size, validate_extension],
                            blank=True,
                            null=True)
    creator = models.ForeignKey(ExtendedUser, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        filename, file_extension = os.path.splitext(self.file.name)
        self.file.name = transliterate.translit(filename, reversed=True) + file_extension

        created = self.pk is None
        super().save(*args, **kwargs)


class TaskComment(models.Model):
    body = models.TextField(max_length=1000)
    creator = models.ForeignKey(ExtendedUser, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

# Create your models here.
