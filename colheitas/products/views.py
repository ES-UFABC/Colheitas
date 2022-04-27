from multiprocessing import Event
from django.shortcuts import redirect, render   
from django.urls import reverse_lazy
from django.views import generic
# from numpy import product
import pkg_resources

# from colheitas.accounts.models import Product
from .models import Product
from .forms import ProductRegisterForm

def delete_product(request, id):
    product_to_delete = Product.objects.get(id=id)
    
    if request.method == 'POST':
        product_to_delete.delete()
        return redirect('product_delete.html')
    
    return render(request, 'delete_confirm.html', {'product': product_to_delete})

# def product_register(request):
#     if request.method == 'POST':
#         form = ProductRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()

#     form = ProductRegisterForm()
#     return render(request, 'products/product_register.html', {'form': form})

class ProductRegisterView(generic.CreateView):
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
   
#    def get_queryset(self):
#        seller = self.request.user.seller
#        products = seller.products