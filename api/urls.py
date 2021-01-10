from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token


router = DefaultRouter()

router.register('create_profile', UserProfileViewset)




urlpatterns = [
                  path('', include(router.urls)),
                  path('login/', UserLoginApiView.as_view()),
                  path('get_all_category/', GetAllCategory.as_view()),
                  path('get_filter_category/', GetFilterCategory.as_view()),
                  path('get_all_product/', GetAllProduct.as_view()),
                  path('get_filter_product/', GetFilterProduct.as_view()),
                  path('get_filter_product_by_category/', ProductFilterByCategory.as_view()),
                  path('token-auth/', obtain_jwt_token)
              ]
