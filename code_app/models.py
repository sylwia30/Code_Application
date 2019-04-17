from django.contrib.auth.models import User
from django.db import models
from users.models import Profile

class Courses(models.Model):
    language_name = models.CharField(max_length=80)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    template_path = models.CharField(max_length=100, default='code_app/python_startcode.html')

    def __str__(self):
        return self.language_name


class Languages(models.Model):
    nr_section = models.IntegerField(unique=True)
    section = models.CharField(max_length=200)
    date_add_language = models.DateTimeField(auto_now_add=True)
    courses = models.ForeignKey(Courses, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.courses.language_name} / {self.section}'


    @property
    def language(self):
        self.courses.language_name

class Exercises(models.Model):
    CHECK_METHODS = (
        (1, 'funkcja'), # wynik kodu
        (2, 'stdout') # wynik treści kodu
    )

    description = models.TextField()
    date_add_exercise = models.DateTimeField(auto_now_add=True)
    section = models.ForeignKey(Languages, on_delete=models.CASCADE, related_name='section_id')
    # metody sprawdzania wyniku
    check_method = models.IntegerField(default=1, choices=CHECK_METHODS)
    check_result = models.TextField(default='')
    check_syntax = models.ManyToManyField("CheckSyntax")

    def __str__(self):
        return f'{self.description}'

    def save(self, *args, **kwargs):
        super(Exercises, self).save(*args, **kwargs)


class CheckSyntax(models.Model):
    name = models.CharField(max_length=64)
    regexp = models.TextField()
    error_message = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class UserExercises(models.Model):
    answer = models.CharField(max_length=5000)
    answer_is_correct = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercises, on_delete=models.CASCADE)
