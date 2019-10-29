from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission
from rest_framework.decorators import action

from api.serializers import ProductSerializer, ServiceSerializer
from api.models import Product, Service


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_update(self, serializer):
        self.permission_classes = (IsAdminUser,)
        self.check_permissions(self.request)
        serializer.save()

    def perform_create(self, serializer):
        self.permission_classes = (IsAdminUser,)
        self.check_permissions(self.request)
        serializer.save()


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def perform_update(self, serializer):
        permission_classes = (IsAdminUser,)
        serializer.save()

    def perform_create(self, serializer):
        permission_classes = (IsAdminUser,)
        serializer.save()


