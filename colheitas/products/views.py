from multiprocessing import Event
from django.shortcuts import redirect, render
from numpy import product
import pkg_resources

from colheitas.accounts.models import Product
from .forms import ProductForm

def delete_product(request, id):
    product_to_delete = Product.objects.get(id=id)
    
    if request.method == 'POST':
        product_to_delete.delete()
        return redirect('product_delete.html')
    
    return render(request, 'products/product_delete_confirmation.html', {'product': product})
    #TODO Product_delete_confirmation, html simples para confirmar o delete

def product_register(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()

    form = ProductForm()
    return render(request, 'products/product_register.html', {'form': form})
