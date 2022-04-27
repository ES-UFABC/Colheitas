from django.urls import path
from django.urls import include, path

# from .views import SignUpView
from .views import ProductRegisterView, ProductsListSeller
from .views import delete_product

urlpatterns = [
    # path('register/', product_register, name='product_register'),
    path('register/', ProductRegisterView.as_view(), name='product_register'),
    path('delete_product/<int:id>/', delete_product, name = 'delete_product'),
    path('products/', ProductsListSeller.as_view(), name='seller_products')
]