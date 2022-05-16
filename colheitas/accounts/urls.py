from django.urls import path
from django.urls import include, path

# from .views import SignUpView
from .views import seller, buyer, signup
from .views.account import private_profile, update_account
from .views.seller import seller_profile


urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path("signup/", signup.SignUpView, name="signup"),
    path('signup/seller/', seller.SellerSignUpView.as_view(), name='seller_signup'),
    path('signup/buyer/', buyer.BuyerSignUpView.as_view(), name='buyer_signup'),
    path('products/', seller.SellerProductsList.as_view(), name='seller_products'),
    path('profile/<int:id>', seller_profile, name='seller_profile'),
    path('private_profile/<int:id>', private_profile, name='private_profile'),
    path('private_profile/<int:id>/Update', update_account, name='update_account')
]