import os
import subprocess
# # Сравнивает пути - чекер - не работает из-за невозможности последовательных команд
# x = r'echo %cd%'
# x_x = os.system(x)
# if x_x == 0:
#     calling_output = subprocess.check_output(x, shell=True)
#     ss = calling_output.decode('cp866')
#     print(ss)
# # Отработка текста ошибки
# x = 'cd unknown'
# x_x = os.system(x)
# if x_x == 1:
#     output = subprocess.getoutput(x)
#     z = output.encode('cp1251')
#     print(z.decode('cp866'))
# отработка тела функции
# ld_1 = str.upper(str.strip(input('Введите наименование локального диска, где создана тестовая директория,\nявляющейся основной для тестирования - туда будет загружен результат тестирования в созданнную скриптом папку result\n')))
# checker = 'echo %cd%'
# while True:
#     fr_main_to_res_p = f'cd {ld_1}://test/main/results/'
#     m_r_p = os.system(fr_main_to_res_p)
#     if m_r_p == 0:
#         x = f'{fr_main_to_res_p} && {checker}'
#         x_x = os.system(x)
#         if x_x == 0:
#             calling_output = subprocess.check_output(x, shell=True)
#             ss = calling_output.decode('cp866')
#             print(ss)
#             z_z = r"\test\main\results"
#             print(f"{ld_1}:" + z_z)
#             break
#             if ss == f"{ld_1}://test/main/results":
#                 with open(results, 'a') as m_r_p_rep:
#                     m_r_rep.write('Переход во вложенный каталог на 1 уровень успешен с указанием полного пути')
#                 break
#     else:
#         with open(results, 'a') as m_r_p_rep:
#             m_r_rep.write('Баг! Переход во вложенный каталог на 1 уровень не осуществлен с указанием полного пути!')
#         break

# Рабочий цикл:
# while True:
#     fr_main_to_res_f = 'cd result'
#     m_r_f = os.system(fr_main_to_res_f)
#     if m_r_f == 0:
#         with open(results, 'a') as m_r_f_rep:
#                     m_r_f_rep.write('Переход во вложенный каталог на 1 уровень успешен с указанием папки')
#         break
#     else:
#         with open(results, 'a') as m_r_f_rep:
#             m_r_f_rep.write('Баг! Переход во вложенный каталог на 1 уровень не осуществлен с указанием папки!')
#         break
