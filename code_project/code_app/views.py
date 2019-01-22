from django.shortcuts import render


def base(request):
    return render(request, 'code_app/base.html')

def start_code(request):
    return render(request, 'code_app/start_code.html')

def courses(request):
    return render(request, 'code_app/courses.html')

def python_cours(request):
    return render(request, 'code_app/python_cours.html')

def html_cours(request):
    return render(request, 'code_app/html_cours.html')

def css_cours(request):
    return render(request, 'code_app/css_cours.html')

def javascript_cours(request):
    return render(request, 'code_app/javascript_cours.html')

def jquery_cours(request):
    return render(request, 'code_app/jquery_cours.html')