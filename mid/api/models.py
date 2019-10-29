from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, User


# class ExtendedUser(AbstractUser):
#     phone = models.CharField(max_length=15, default='')
#
#     class Meta:
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)
    address = models.CharField(max_length=300)
    address2 = models.CharField(max_length=300)
    registration_date = models.DateTimeField(auto_now_add=True)


class ProductServiceBase(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


productTypes = (
    (1, 'Type1'),
    (2, 'Type2'),
    (3, 'Type3'),
)

serviceTypes = (
    (1, 'Type1'),
    (2, 'Type2'),
    (3, 'Type3'),
)

class Product(ProductServiceBase):
    size = models.IntegerField()
    type = models.PositiveSmallIntegerField(choices=productTypes)
    existence = models.IntegerField()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Service(ProductServiceBase):
    approximate_duration = models.IntegerField()
    type = models.PositiveSmallIntegerField(choices=serviceTypes)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
