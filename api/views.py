from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, \
    UpdateModelMixin
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from .permissions import *
from rest_framework import viewsets


class UserProfileViewset(viewsets.ModelViewSet):
    """Handle create and update profile"""
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)


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
    filter_fields = ('category__id', 'category__name',)


class UserLoginApiView(ObtainAuthToken):
    # """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
