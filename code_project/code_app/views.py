from django.shortcuts import render


def base(request):
    return render(request, 'code_app/base.html')

