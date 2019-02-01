# metoda sprawdzania samego wyniku
import subprocess

class Checker:

    @staticmethod
    def check_by_function(function_code, correct_answer_checker):

        f = open("/tmp/student_answer.py", "w")
        f.write(function_code)

        f.write("\n")
        f.write(correct_answer_checker)

        f.close()

        ret = subprocess.run(["python3", "/tmp/student_answer.py"])
        print("RET", ret.returncode)

        if ret.returncode == 0:
            return True

        return False

    # @staticmethod
    # def check_syntax(student_code, check_syntax_code):

''''
ret = wynik(3)
import sys
if ret == 9:
    sys.exit(0)
else:
    sys.exit(-1)
'''

import re
text = """


def aaa():
444
    aaa tt2returnaaa x*x
    scnakc
    
    
ASc
"""

pattern = re.compile(r'\n*return.*')
matcher = pattern.search(text)
if pattern.search(text) == None:
    print("w funkcji nie ma 'return'")
else:
    print("Znaleziono return w kodzie")



# class ExerciseView222(LoginRequiredMixin, View):
#     def get(self, request, pk):
#         exercise = Exercises.objects.get(pk=pk)
#         next_exercise = Exercises.objects.get(pk=exercise.pk +1)
#         return render(request, 'code_app/python222.html', {"exercise":exercise,
#                                                            "next_exercise": next_exercise,
#                                                            })
#
#     def post(self, request, pk):
#         answer = request.POST.get("answer")
#         save_answer = UserExercises.objects.create(student_id=request.user.pk, exercise_id=1, answer=answer)
#         syntax = Exercises.objects.filter(id=pk)
#         for i in syntax:
#             for j in i.check_syntax.all():
#                 print(j.name)
#                 # pattern = re.compile(j.regexp)
#                 # pattern = re.compile(r'^[A-Za-z0-9 _\s]+[A-Za-z0-9\s]+[A-Za-z0-9 _\s]+return+[\sA-Za-z0-9 _\s]+[A-Za-z0-9\s]+[A-Za-z0-9 _\s]+$')
#                 pattern = re.compile(r'\n*return.*')
#                 print(pattern)
#                 print(answer)
#                 x= pattern.search(answer)
#                 print(x)
#                 if pattern.search(answer) == None:
#                     messages.error(request, j.error_message)
#                     return render(request, 'code_app/python222.html', locals())
#                 else:
#                     messages.success(request, f'Super! Zadanie prawidłowo rozwiązane :)')
#                     return render(request, 'code_app/python222.html', locals())
#         check_result_answer = Checker.check_by_function(answer, save_answer.exercise.check_result)
#         if check_result_answer:
#             save_answer.answer_is_correct = True
#             save_answer.save()
#             messages.success(request, f'Brawo! Zadanie prawidłowo rozwiązane')
#         else:
#             messages.error(request, f'Niestety nie udało się, spróbuj jeszcze raz!')
#         return render(request, 'code_app/python222.html', locals())