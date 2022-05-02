from django.urls import path
from django.urls import include, path

# from .views import SignUpView
from .views import seller, buyer, signup


urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path("signup/", signup.SignUpView, name="signup"),
    path('signup/seller/', seller.SellerSignUpView.as_view(), name='seller_signup'),
    path('signup/buyer/', buyer.BuyerSignUpView.as_view(), name='buyer_signup'),
    path('products/', seller.SellerProductsList.as_view(), name='seller_products')
]