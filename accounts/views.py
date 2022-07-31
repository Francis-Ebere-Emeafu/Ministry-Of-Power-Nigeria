from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required


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


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                messages.warning(request, "Invalid username or password")
                return redirect('login')
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {"form": form})


def logout_user(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def profile(request):

    context = {
        # "account": account,
        # "day_of_week": day_of_week,
        # "daytime": daytime,
        # "greeting": greeting,
    }
    return render(request, 'accounts/profile.html', context)