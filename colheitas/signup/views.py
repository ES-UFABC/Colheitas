from django.shortcuts import render
from .forms import SellerForm


# Create your views here.
def signup(request):
    return render(request, 'signup/signup.html')


def buyer_signup(request):
    return render(request, 'signup/buyer_signup.html')


def seller_signup(request):
    if request.method == 'POST':
        form = SellerForm(request.POST)
        if form.is_valid():
            form.save()

    form = SellerForm()
    return render(request, 'signup/seller_signup.html', {'form': form})
