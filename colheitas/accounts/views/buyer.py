from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth import login
from django.shortcuts import redirect

from ..forms import BuyerSignUpForm
from ..models import User

class BuyerSignUpView(generic.CreateView):
    model = User
    form_class = BuyerSignUpForm
    
    success_url = reverse_lazy("login")
    template_name = "registration/signup_buyer.html"

    # def get_context_data(self, **kwargs):
    #     kwargs['user_type'] = 'seller'
    #     return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/accounts/login/')