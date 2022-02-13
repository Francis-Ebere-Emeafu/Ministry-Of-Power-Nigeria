
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ObjectDoesNotExist

from accounts.models import Account


class RegForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(max_length=50, widget=forms.PasswordInput, validators=[validate_password])
    confirm = forms.CharField(max_length=50, widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ['first_name', 'surname', 'phone', 'department']

    def clean_email(self):
        if 'email' in self.cleaned_data:
            email = self.cleaned_data['email']
            try:
                User.objects.get(username=email)
            except User.DoesNotExist:
                return email
            else:
                raise forms.ValidationError("The email address has been taken!")

    def clean(self):
        if 'password' in self.cleaned_data and 'confirm' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['confirm']:
                raise forms.ValidationError("The passwords do not match!")
            return self.cleaned_data



class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)

    def clean(self):
        if 'username' in self.cleaned_data and 'password' in self.cleaned_data:
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            user = authenticate(username=username, password=password)
            print('---------DONE---------', user, '---------DONE---------')

            if user is not None:
                print('Returning User')
                return self.cleaned_data
            elif user == "None":
                print('Raising Error')
                raise forms.ValidationError('Wrong username or password')
           