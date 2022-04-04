from django.urls import path
from django.urls import include, path

# from .views import SignUpView
from .views import product_register


urlpatterns = [
    path('register/', product_register, name='product_register')
]