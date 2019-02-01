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
    python_describe = Courses.objects.get(pk=1)
    html_describe = Courses.objects.get(pk=2)
    css_describe = Courses.objects.get(pk=3)
    js_describe = Courses.objects.get(pk=4)
    jquery_describe = Courses.objects.get(pk=5)
    return render(request, 'code_app/courses.html', {"python_describe": python_describe,"html_describe": html_describe,
                                                     "css_describe": css_describe, "js_describe": js_describe,
                                                     "jquery_describe": jquery_describe,
                                                     })

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
    return render(request, course.template_path, {"form":form, 'last_exercise': last_exercise, "course": course})

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
            messages.success(request, f'Zadanie prawidłowo rozwiązane')
        else:
            messages.success(request, f'Zadanie nieprawidlowo rozwiazane')
        return render(request, 'code_app/python_exercise.html', locals())
# to powinno byc ajaksem narazie robimy prostsza wersje

class PythonCourseAllView(LoginRequiredMixin, View):
    def get(self, request, pk):
        language_sections = Languages.objects.filter(courses=1)
        exer = Exercises.objects.filter(section__courses=1).order_by('id').first()
        return render(request, 'code_app/python_course_exercises.html', {"language_sections": language_sections})


class ExerciseView222(LoginRequiredMixin, View):
    def get(self, request, pk):
        exercise = Exercises.objects.get(pk=pk)
        next_exercise = Exercises.objects.get(pk=exercise.pk +1)
        return render(request, 'code_app/python222.html', {"exercise":exercise,
                                                           "next_exercise": next_exercise,
                                                           })

    def post(self, request, pk):
        answer = request.POST.get("answer")
        save_answer = UserExercises.objects.create(student_id=request.user.pk, exercise_id=1, answer=answer)
        syntax = Exercises.objects.filter(id=pk)
        for i in syntax:
            for j in i.check_syntax.all():
                print(j.name)
                # pattern = re.compile(j.regexp)
                # pattern = re.compile(r'^[A-Za-z0-9 _\s]+[A-Za-z0-9\s]+[A-Za-z0-9 _\s]+return+[\sA-Za-z0-9 _\s]+[A-Za-z0-9\s]+[A-Za-z0-9 _\s]+$')
                pattern = re.compile(r'^[.\n]+return+[.\n]')
                print(pattern)
                print(answer)
                x= pattern.fullmatch(answer)
                print(x)
                if pattern.fullmatch(answer) == None:
                    messages.error(request, j.error_message)
                    return render(request, 'code_app/python222.html', locals())
                else:
                    messages.success(request, f'Super! Zadanie prawidłowo rozwiązane :)')
                    return render(request, 'code_app/python222.html', locals())
        check_result_answer = Checker.check_by_function(answer, save_answer.exercise.check_result)
        if check_result_answer:
            save_answer.answer_is_correct = True
            save_answer.save()
            messages.success(request, f'Brawo! Zadanie prawidłowo rozwiązane')
        else:
            messages.error(request, f'Niestety nie udało się, spróbuj jeszcze raz!')
        return render(request, 'code_app/python222.html', locals())


def html_cours(request):
    html_sections = Languages.objects.filter(courses_id=2)
    return render(request, 'code_app/html_cours.html', {"html_sections": html_sections})

def html_start_code(request):
    return render(request, 'code_app/html_startcode.html')

def css_cours(request):
    css_sections = Languages.objects.filter(courses_id=3)
    return render(request, 'code_app/css_cours.html', {"css_sections": css_sections})

def javascript_cours(request):
    js_sections = Languages.objects.filter(courses_id=4)
    return render(request, 'code_app/javascript_cours.html', {"js_sections": js_sections})

def jquery_cours(request):
    jq_sections = Languages.objects.filter(courses_id=5)
    return render(request, 'code_app/jquery_cours.html', {"jq_sections": jq_sections})

def liczby(request):
    return render(request, 'code_app/liczby.html')