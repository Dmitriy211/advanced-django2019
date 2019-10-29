from rest_framework import serializers
from .models import Product, Service, Profile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )

        user.set_password(validated_data['password'])
        user.save()

        profile = Profile.objects.create(
            user=user
        )
        profile.save()
        return user


    class Meta:
        model = User
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False)

    def create(self, validated_data):
        product = Product.objects.create(
            name=validated_data['name'],
            price=validated_data['price'],
            description=validated_data['description'],
            size=validated_data['size'],
            type=validated_data['type'],
            existence=validated_data['existence'],
        )

        if (product.size < 20 or product.size > 50):
            raise TypeError("nope")

        product.save()
        return product

    class Meta:
        model = Product
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False)

    def create(self, validated_data):
        service = Service.objects.create(
            name=validated_data['name'],
            price=validated_data['price'],
            description=validated_data['description'],
            approximate_duration=validated_data['approximate_duration'],
            type=validated_data['type'],
        )

        if (service.approximate_duration < 0):
            raise TypeError("nope")

        service.save()
        return service

    class Meta:
        model = Service
        fields = '__all__'
