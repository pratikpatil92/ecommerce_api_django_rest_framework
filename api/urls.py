from django.urls import path, include
from .views import *

urlpatterns = [
    path('create_user/', UserCreate.as_view()),
    path('get_all_category/', GetAllCategory.as_view()),
    path('get_filter_category/', GetFilterCategory.as_view()),
    path('get_all_product/', GetAllProduct.as_view()),
    path('get_filter_product/', GetFilterProduct.as_view()),
]