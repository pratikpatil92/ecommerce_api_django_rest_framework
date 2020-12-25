from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, \
    UpdateModelMixin
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics


class UserCreate(GenericAPIView, CreateModelMixin):
    """This class use to create new user"""
    queryset = UserProfile.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class GetAllCategory(GenericAPIView, ListModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class GetFilterCategory(GenericAPIView, ListModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategoryFilterSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class GetAllProduct(GenericAPIView, ListModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class GetFilterProduct(GenericAPIView, ListModelMixin):
    queryset = Product.objects.filter()
    serializer_class = ProductFilterSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProductFilterByCategory(generics.ListAPIView):
    serializer_class = ProductFilterSerializer
    queryset = Product.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('category__id','category__name',)


