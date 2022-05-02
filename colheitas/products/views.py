from multiprocessing import Event
from django.shortcuts import redirect, render   
from django.urls import reverse_lazy
from django.views import generic
import pkg_resources
from django.contrib.auth.mixins import UserPassesTestMixin

# from colheitas.accounts.models import Product
from .models import Product
from .forms import ProductRegisterForm

def delete_product(request, id):
    product_to_delete = Product.objects.get(id=id)
    product_to_delete.delete()
    return redirect('seller_products')

def search_product(request):
    if request.method == "POST":
        searched = request.POST['searched']
        products = Product.objects.filter(name__contains =searched)
        return render(request, 'products/search_product.html', {'searched': searched, 'products': products})
    else:
        # todo redirecionar para 404
        products = Product.objects.all()
        return render(request, 'products/search_product.html', {'products': products})

# def product_register(request):
#     if request.method == 'POST':
#         form = ProductRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()

#     form = ProductRegisterForm()
#     return render(request, 'products/product_register.html', {'form': form})


class ProductRegisterView(UserPassesTestMixin, generic.CreateView):

    def test_func(self):
        return self.request.user.user_type == 1

    model = Product
    form_class = ProductRegisterForm

    success_url = reverse_lazy('/')
    template_name = 'products/product_register.html'

    def get_form_kwargs(self):
        kwargs = super(ProductRegisterView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        product = form.save()
        return redirect('/')

class ProductsListSeller(generic.ListView):
    model = Product
    
    def get_queryset(self):
        queryset = Product.objects.filter(seller=self.request.user.seller)
        return queryset

def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'products/product_detail.html', {'product':product})

def delete_confirm(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'products/delete_confirm.html', {'product':product})
   
#    def get_queryset(self):
#        seller = self.request.user.seller
#        products = seller.products