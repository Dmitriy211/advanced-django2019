from django.contrib import admin
from .models import Article, ArticleImage, FavoriteArticle


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'creator')

@admin.register(ArticleImage)
class ArticleImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'article')


@admin.register(FavoriteArticle)
class FavoriteArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'user')
