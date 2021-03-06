from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
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

def start_code_get(request, pk):
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
        check_result_answer = Checker.check_by_function(answer, save_answer.exercise.check_result)
        if check_result_answer:
            save_answer.answer_is_correct = True
            save_answer.save()
            messages.success(request, f'Zadanie prawidłowo rozwiązane')
        else:
            messages.success(request, f'Zadanie nieprawidlowo rozwiazane')
        return render(request, 'code_app/python_exercise.html', locals())


class PythonCourseAllView(LoginRequiredMixin, View):
    def get(self, request, pk):
        language_sections = Languages.objects.filter(courses=1)
        exer = Exercises.objects.filter(section__courses=1).order_by('id').first()
        return render(request, 'code_app/python_course_exercises.html', {"language_sections": language_sections})


class ExerciseView222(LoginRequiredMixin, View):
    def get(self, request, pk):
        exercise = Exercises.objects.get(pk=pk)
        # next_exercise = Exercises.objects.get(pk=exercise.pk +1)
        next_exercise = pk + 1
        return render(request, 'code_app/python222.html', {"exercise":exercise,
                                                           "next_exercise": next_exercise,
                                                           })
    def post(self, request, pk):
        answer = request.POST.get("answer")
        save_answer = UserExercises.objects.create(student_id=request.user.pk, exercise_id=pk, answer=answer)
        syntax = Exercises.objects.filter(id=pk)
        for i in syntax:
            for j in i.check_syntax.all():
                print(j.name)
                pattern = re.sub(r'\\(.)', r'\1', j.regexp)
                pattern = re.compile(pattern)
                print(pattern)
                print(answer)
                x= pattern.search(answer)
                print(x)
                if pattern.search(answer) == None:
                    messages.error(request, j.error_message)
                    return redirect('python222', pk)
            check_result_answer = Checker.check_by_function(answer, save_answer.exercise.check_result)
            if check_result_answer:
                save_answer.answer_is_correct = True
                save_answer.save()
                messages.success(request, f'Brawo! Zadanie prawidłowo rozwiązane')
                return redirect('python222', pk+1)
            else:
                messages.error(request, f'Niestety nie udało się, spróbuj jeszcze raz!')
            return redirect('python222', pk)

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

class liczby(LoginRequiredMixin):
    def liczby_test(request):
        return render(request, 'code_app/liczby.html')