from django.urls import path
from django.urls import include, path

# from .views import SignUpView
from .views import ProductRegisterView, ProductsListSeller, ProductListState
from .views import delete_product, product_detail

urlpatterns = [
    # path('register/', product_register, name='product_register'),
    path('register/', ProductRegisterView.as_view(), name='product_register'),
    path('delete_product/<int:id>/', delete_product, name = 'delete_product'),
    path('products/', ProductsListSeller.as_view(), name='seller_products'),
    path('products/<int:id>', product_detail, name='product_detail'),
    path('products/state/', ProductListState.as_view(), name='state_products')
    
]