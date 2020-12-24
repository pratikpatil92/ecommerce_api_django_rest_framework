from rest_framework import serializers

from .models import *


class RegisterSerializer(serializers.ModelSerializer):
    """User create serializer"""

    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'is_staff': {'read_only': True},
            'password': {'write_only': True},
        }


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name',)


class CategoryFilterSerializer(serializers.ModelSerializer):
    category_name = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'category_name')


class ProductFilterSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('id', "category", "title", "price", "description", "brand", "image")
