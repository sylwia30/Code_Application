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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users.views import LoginUserView, register, ProfileView, profile, UserDeleteForm
from code_app.views import base, start_code, courses, python_cours, html_cours, css_cours, javascript_cours, \
    jquery_cours, html_start_code, start_code_get, ExerciseView, PythonCourseAllView, ExerciseView222

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat.urls')),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', profile, name='profile-edit'),
    path('profile/<int:pk>/delete/', UserDeleteForm.as_view(template_name='users/user_confirm_delete.html'),
         name='user-delete'),
    path('', base, name='base'),
    path('start_code/', start_code, name="start-code"),
    path('courses/', courses, name="courses"),
    path('python/', python_cours, name="python-cours"),
    path('python_cours/<int:pk>/', start_code_get, name="python-start-cours"),
    path('python/<int:pk>/', ExerciseView.as_view(), name="python-exercise"),
    path('html/', html_cours, name="html-cours"),
    path('html_cours/', html_start_code, name="html-start-cours"),
    path('css/', css_cours, name="css-cours"),
    path('javascript/', javascript_cours, name="javascript-cours"),
    path('jquery/', jquery_cours, name="jquery-cours"),

    path('python_course_exercises/<int:pk>/', PythonCourseAllView.as_view(), name="python-course-exercises"),
    path('python222/<int:pk>/', ExerciseView222.as_view(), name="python222"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    """ to pozwala na wyświetlenie obrazka w profilu """