from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth import login
from django.shortcuts import redirect, render

from ..forms import SellerSignUpForm
from ..models import User, Seller
from products.models import Product

class SellerSignUpView(generic.CreateView):
    model = User
    form_class = SellerSignUpForm
    
    success_url = reverse_lazy("login")
    template_name = "registration/signup_seller.html"
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/accounts/login/')

class SellerProductsList(generic.ListView):
    model = Seller
    queryset = Seller.products
   
def seller_profile(request, id):
    seller = Seller.objects.get(user_id=id)
    return render(request, 'profile.html', {'seller':seller})