from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import  Layout, Submit
from .models import Seller, Certifications


class SellerForm(forms.ModelForm):

    class Meta:
        model = Seller
        fields = ('name', 'fantasy_name', 'cpf_cnpj', 'collective_or_individual','state', 'region', 'cep_production', 'address_number_production', 'cep_comerce' ,'address_number_comerce',
                  'have_certification', 'certifications', 'ecological', 'ecological_certification', 'organic', 'indigenous_recognizing', 'quilombola_recognizing')

        certifications = forms.ModelMultipleChoiceField(
            queryset=Certifications.objects.all(),
            widget=forms.CheckboxSelectMultiple
        )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'
