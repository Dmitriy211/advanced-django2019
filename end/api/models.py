from django.db import models
from django.contrib.auth.models import User


def image_path(instance, filename):
    return f'images/{instance.article.id}/{filename}'

# Create your models here.

class Article(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=1000)
    price = models.IntegerField()
    city = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    color = models.PositiveSmallIntegerField(choices=((1, 'red'), (2, 'green'), (3, 'blue')), default=1)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.name


class ArticleImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    image = models.FileField(upload_to=image_path, blank=True, null=True)


class FavoriteArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)