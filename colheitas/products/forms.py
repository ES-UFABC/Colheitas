from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import  Layout, Submit
from .models import Product, Typology


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product

        # typology = forms.ModelMultipleChoiceField(
        #     queryset=Typology.objects.all().values('name'),
        #     widget=forms.CheckboxSelectMultiple

        # )

        fields = ('name', 'measure', 'price') # , 'typology')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'
