from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import  Layout, Submit
from .models import Product, Typology


class ProductRegisterForm(forms.ModelForm):
    name = forms.CharField(required=True, max_length=200)
    price = forms.FloatField(required=True)
    # measure = forms.ModelMultipleChoiceField(choices = Product.MEASURE)
    
    class Meta:
        model = Product
        # typology = forms.ModelMultipleChoiceField(
        #     queryset=Typology.objects.all().values('name'),
        #     widget=forms.CheckboxSelectMultiple

        # )
        fields = ('name', 'quantity', 'measure', 'price') # , 'typology')

    def __init__(self, *args, **kwargs):
        # super().__init__(*args, **kwargs)
        # self.helper = FormHelper
        # self.helper.form_method = 'post'
        self.request = kwargs.pop('request')
        super(ProductRegisterForm, self).__init__(*args, **kwargs)
        # self.fields['user'].queryset = Product.objects.filter(user=self.request.user)
        

    def save(self):
        product = super().save(commit=False)
        product.name = self.cleaned_data['name']
        product.price = self.cleaned_data['price']
        # product.measure = self.cleaned_data['measure']
        product.quantity = self.cleaned_data['quantity']
        product.seller = self.request.user.seller
        product.state = self.request.user.state
        product.save()
        return product