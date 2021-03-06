"""colheitas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf   
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
# from accounts.views import seller, buyer

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    # path('', include('landing_page.urls')),
    path("accounts/", include("accounts.urls")),
    # path('signup/', include('signup.urls')),    
    path('admin/', admin.site.urls),
    path('products/', include("products.urls")),
    # path('accounts/', include("django.contrib.auth.urls")), 
    # path('accounts/signup/', include('accounts.urls')),
    # path('accounts/signup/seller/', seller.SellerSignUpView.as_view(), name='seller_signup'),
    # path('accounts/signup/buyer/', buyer.BuyerSignUpView.as_view(), name='buyer_signup'),
]
