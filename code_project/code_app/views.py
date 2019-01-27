from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import Languages, Exercises, UserExercises, Courses
from django.views import View
from .checker import Checker
import re


def base(request):
    return render(request, 'code_app/base.html')

def start_code(request):
    return render(request, 'code_app/start_code.html')

def courses(request):
    return render(request, 'code_app/courses.html')

def python_cours(request):
    return start_code_get(request, 1)
    # for i in form:
    #     a = i.section_id.all()
    #     print(a)
    #     for j in a:
    #         print(j)

def start_code_get(request, pk):
    ''' Lista rozdzialow '''
    course = Courses.objects.get(pk=pk)
    form = Languages.objects.filter(courses = course)

    last_exercise = Exercises.objects.filter(section__courses=course).order_by('id').first()

    return render(request, course.template_path, {"form":form, 'last_exercise': last_exercise})

class ExerciseView(LoginRequiredMixin, View):
    def get(self, request, pk):
        exercise = Exercises.objects.get(pk=pk)
        return render(request, 'code_app/python_exercise.html', {"exercise":exercise})

    def post(self, request, pk):
        answer = request.POST.get("answer")
        save_answer = UserExercises.objects.create(student_id=request.user.pk, exercise_id=1, answer=answer)
        syntax = Exercises.objects.filter(id=pk)
        for i in syntax:
            for j in i.check_syntax.all():
                print(j.name)
                pattern = re.compile(j.regexp)
                if pattern.fullmatch(answer) == None:
                    messages.error(request, j.error_message)
                    return render(request, 'code_app/python_exercise.html', locals())
        ###
        # pattern = re.compile("o")
        ###
        # >> >
        # >> > pattern.match("dog")  # No match as "o" is not at the start of "dog".
        # >> > pattern.match("dog", 1)  # Match as "o" is the 2nd character of "dog".
        # < re.Match
        # object;
        # span = (1, 2), match = 'o' >

        check_result_answer = Checker.check_by_function(answer, save_answer.exercise.check_result)
        if check_result_answer:
            save_answer.answer_is_correct = True
            save_answer.save()
            messages.success(request, f'zadanie prawidłowo rozwiązane')
        else:
            messages.success(request, f'zadanie nieprawidlowo rozwiazane')
        return render(request, 'code_app/python_exercise.html', locals())



# to powinno byc ajaksem narazie robimy prostsza wersje


def html_cours(request):
    return render(request, 'code_app/html_cours.html')

def html_start_code(request):
    return render(request, 'code_app/html_startcode.html')

def css_cours(request):
    return render(request, 'code_app/css_cours.html')

def javascript_cours(request):
    return render(request, 'code_app/javascript_cours.html')

def jquery_cours(request):
    return render(request, 'code_app/jquery_cours.html')