from django.urls import path
from django.urls import include, path

# from .views import SignUpView
from .views import delete_confirm  # product_register
from .views import search_product
from .views import ProductRegisterView, ProductsListSeller, ProductListState
from .views import delete_product, product_detail,update_product

urlpatterns = [
    # path('register/', product_register, name='product_register'),
    path('register/', ProductRegisterView.as_view(), name='product_register'),
    path('update_product/<int:id>/', update_product, name = 'update_product'),
    path('delete_product/<int:id>/', delete_product, name = 'delete_product'),
    path('delete_confirm/<int:id>/', delete_confirm, name = 'delete_confirm'),
    path('search_product/', search_product, name = 'search_product'),
    path('products/', ProductsListSeller.as_view(), name='seller_products'),
    path('products/<int:id>', product_detail, name='product_detail'),
    path('products/state/', ProductListState.as_view(), name='state_products')

]