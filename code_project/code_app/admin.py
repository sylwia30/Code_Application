from django.contrib import admin

from .models import Exercises, Courses, CheckSyntax

admin.site.register(Exercises)

admin.site.register(Courses)

admin.site.register(CheckSyntax)