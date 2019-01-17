"""code_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from code_app.views import base
from users.views import LoginUserView, register, ProfileView, profile, UserDeleteForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base, name='base'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', profile, name='profile-edit'),
    path('profile/<int:pk>/delete/', UserDeleteForm.as_view(template_name='users/user_confirm_delete.html'),
         name='user-delete'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    """ to pozwala na wyświetlenie obrazka w profilu """