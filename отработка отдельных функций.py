import os
import subprocess
# Сравнивает пути - чекер
x = 'echo %cd%'
x_x = os.system(x)
if x_x == 0:
    calling_output = subprocess.check_output(x, shell=True)
    ss = calling_output.decode('cp866')
    print(ss)
# Отработка текста ошибки
# x = 'cd unknown'
# x_x = os.system(x)
# if x_x == 1:
#     output = subprocess.getoutput(x)
#     z = output.decode('cp1251')
#     print(z.decode('cp866'))
