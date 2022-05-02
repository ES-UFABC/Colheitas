from multiprocessing import Event
from django.shortcuts import redirect, render   
from django.urls import reverse_lazy
from django.views import generic
import pkg_resources
from django.contrib.auth.mixins import UserPassesTestMixin

# from colheitas.accounts.models import Product
from .models import Product
from .forms import ProductRegisterForm

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
    template_name = 'products/product_list_seller.html'

    def get_queryset(self):
        queryset = Product.objects.filter(seller=self.request.user.seller)
        return queryset

class ProductListState(generic.ListView):
    model = Product
    template_name = 'products/product_list_state.html'
    
    def get_queryset(self):
        queryset = Product.objects.filter(state=self.request.user.state)
        return queryset

def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'products/product_detail.html', {'product':product})

def delete_product(request, id):
    product_to_delete = Product.objects.get(id=id)
    
    if request.method == 'POST':
        product_to_delete.delete()
        return redirect('product_delete.html')
    
    return render(request, 'delete_confirm.html', {'product': product_to_delete})