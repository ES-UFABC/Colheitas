from django.shortcuts import render
from .forms import ProductForm


def product_register(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()

    form = ProductForm()
    return render(request, 'products/product_register.html', {'form': form})
