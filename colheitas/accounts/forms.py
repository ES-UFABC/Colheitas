from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from localflavor.br.forms import BRStateChoiceField
from .models import User, Seller, Product

class SellerSignUpForm(UserCreationForm):
    state = BRStateChoiceField()
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=256)
    last_name = forms.CharField(max_length=256)
    # product = forms.ModelMultipleChoiceField(queryset=Product.objects.all() ,required=False)

    class Meta(UserCreationForm.Meta):
        model = User 
        field = (
            'username',
            'first_name',
            'last_name',
            'state',
            'password1',
            'password2'
        )

    def save(self):
        user = super().save(commit=False)
        user.user_type = 1
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.state = self.cleaned_data['state']

        user.save()
        # create associated seller info
        seller = Seller.objects.create(user=user)
        return user

class BuyerSignUpForm(UserCreationForm):
    state = BRStateChoiceField()
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=256)
    last_name = forms.CharField(max_length=256)
    # product = forms.ModelMultipleChoiceField(queryset=Product.objects.all() ,required=False)

    class Meta(UserCreationForm.Meta):
        model = User 
        field = (
            'username',
            'first_name',
            'last_name',
            'state',
            'password1',
            'password2'
        )

    def save(self):
        user = super().save(commit=False)
        user.user_type = 2
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.state = self.cleaned_data['state']

        user.save()
        return user