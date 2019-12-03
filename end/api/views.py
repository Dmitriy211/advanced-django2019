from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser

from .serializers import ArticleShortSerializer, ArticleFullSerializer, ArticleImageSerializer
from .models import Article, ArticleImage, FavoriteArticle
import logging

logger = logging.getLogger(__name__)


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleFullSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
        logger.info(f"{self.request.user} created article {serializer.data.get('id')}: {serializer.data.get('name')}")

    @action(methods=['GET'], detail=True)
    def images(self, request, pk):
        images = Article.objects.get(id=pk).articleimage_set.all()
        serializer = ArticleImageSerializer(images, many=True)
        return Response(serializer.data)

    # @action(methods=['POST'], detail=True)
    # def favorites(self, request, pk):
    #     article = Article.objects.get(id=pk)
    #     favorites = FavoriteArticle.objects.filter(user=self.request.user)
    #     serializer = ArticleShortSerializer(favorites, many=True)
    #     return Response(serializer.data)

    @action(methods=['GET'], detail=False)
    def favorites(self, request):
        favorites = FavoriteArticle.objects.filter(user=self.request.user)
        serializer = ArticleShortSerializer(favorites, many=True)
        return Response(serializer.data)


class ArticleImageViewSet(viewsets.GenericViewSet,
                          mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin):
    serializer_class = ArticleImageSerializer
    queryset = ArticleImage.objects.all()
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser, JSONParser,)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
        logger.info(
            f"'{self.request.user}' added image '{serializer.data.get('id')}: {serializer.data.get('file_name')}' "
            f"for article '{serializer.data.get('article')}'"
        )
