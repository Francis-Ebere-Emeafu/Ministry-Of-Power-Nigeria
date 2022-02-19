
from tkinter import Widget
from django import forms
from django.core.exceptions import ObjectDoesNotExist

from company.models import Company


class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ['company_name', 'address', 'website', 'email', 'phone', 'name', 'logo']

        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'row':3, 'placeholder': 'Address of Company'}),
            'website': forms.URLField(attrs={'class': 'form-control', 'placeholder': 'Website'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Person'}),
            'logo': forms.ImageField(attrs={'class': 'form-control', 'placeholder': 'Logo'}),
        }

    def clean_company_name(self):
        if 'company_name' in self.cleaned_data:
            company_name = self.cleaned_data['company_name']
            try:
                Company.objects.get(company_name=company_name)
            except Company.DoesNotExist:
                return company_name
            else:
                raise forms.ValidationError("This company has already been registered!")

    