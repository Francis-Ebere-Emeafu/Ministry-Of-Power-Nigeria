from django.contrib.auth.models import User
from django.shortcuts import render


from accounts.models import Account
from accounts.forms import RegForm, LoginForm


def register(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            username = form.cleaned_data['email']

            new_user = User.objects.create_user(
                username=username, password=password)
            new_user.is_active = False
            new_user.save()

            account = form.save(commit=False)
            account.user = new_user
            account.email = username
            account.save()
            
    else:
        form = RegForm()
    return render(request, "accounts/register.html", {"form": form})
