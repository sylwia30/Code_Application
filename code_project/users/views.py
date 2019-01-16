from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from django.contrib import messages
from django.views import View
from django.views.generic import ListView

from users.forms import UserRegisterForm, LoginForm
from users.models import Profile


class LoginUserView(View):
    form_class = LoginForm

    def get(self, request):
        return render(request, 'users/login.html', {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = User.objects.filter(email=email.lower()).first()
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Witaj {username}!')
                return redirect('base')
            else:
                messages.warning(request, 'Błędny login lub hasło')
        return render(request, 'users/login.html', {'form': self.form_class})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Konto zostało utworzone! Możesz się zalogować!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


class ProfileView(View):
    def get(self, request, id):
        profile = get_object_or_404(User, id=id)
        return render(request, 'users/profile.html', {'profile': profile})





