from django.urls import path

from . import views

urlpatterns = [
    # /signup/
    path('', views.signup, name='signup'),
    # /signup/buyer/
    path('buyer/', views.buyer_signup, name='buyer'),
    # /signup/seller/
    path('seller/', views.seller_signup, name='seller'),
]