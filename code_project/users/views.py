from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib import messages
from django.views import View

from users.forms import UserRegisterForm, LoginForm


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

# nie mogę zmienić aby pojawiał się taki sam komunikat jak w przypadku logowania, zielony alert!
# class LogoutView2(LogoutView, View):
#
#     def logout(self, request):
#         messages.success(request, f'Użytkownik został wylogowany!')
#         return render(request, 'users/logout.html')