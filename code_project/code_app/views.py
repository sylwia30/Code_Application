from django.shortcuts import render


def base(request):
    return render(request, 'code_app/base.html')

def start_code(request):
    return render(request, 'code_app/start_code.html')