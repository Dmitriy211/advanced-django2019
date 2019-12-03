from rest_framework import serializers
from .models import Article, ArticleImage, FavoriteArticle
from .validators import validate_extension, validate_file_size
import re


class ArticleShortSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'name')


class ArticleFullSerializer(ArticleShortSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False)

    creator_name = serializers.SerializerMethodField(read_only=True)
    creator = serializers.HiddenField(required=False, default=serializers.CurrentUserDefault())

    images = serializers.SerializerMethodField(read_only=True)

    class Meta(ArticleShortSerializer.Meta):
        fields = '__all__'

    def get_creator_name(self, obj):
        if obj.creator is not None:
            return obj.creator.username
        return ''

    def get_images(self, obj):
        if obj.articleimage_set is not None:
            return obj.articleimage_set
        return ''



class ArticleImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    image = serializers.FileField(required=True)
    article = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ArticleImage
        fields = '__all__'

    def get_file_name(self, obj):
        if obj.file.name is not None:
            return obj.file.name
        return ''

    def validate_image(self, value):
        validate_file_size(value)
        validate_extension(value)
        return value