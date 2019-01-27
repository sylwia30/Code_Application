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