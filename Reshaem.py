import os
import subprocess
import sys
import argparse
from datetime import datetime
from datetime import date
# Создание директорий - выведем в батник и настроим стартовую директорию оттуда
# Введите названия дисков на латинском через пробел
while True:
    ld_1 = str.upper(str.strip(input('Введите наименование локального диска, где создана тестовая директория,\nявляющейся основной для тестирования - туда будет загружен результат тестирования\n в созданнную скриптом папку result\n')))
    ld_2 = str.upper(str.strip(input('Введите наименование другого диска, где создана побочная тестовая директория,\nнеобходимая для тестирования перехода между локальными дисками\n')))
    if ld_1 == ld_2:
        print('Значения не могут быть равны')
    else:
        break
# Создадим файл для отчетности
result_path = f"{ld_1}://test/main/results/"
curr_date = str(date.today())
title_results = f'results_{curr_date}.txt'
results = result_path + title_results
r = open(results, 'w')
r.write('Здесь хранятся результаты тестирования')
r.close()
# Начинаем тестирование из предварительно настроенной стартовой директории (main)
# Создадим чекер
checker = 'echo %cd%'
# Переход из main во вложенный каталог - result с помощью указания папки
while True:
    fr_main_to_res_f = 'cd result'
    m_r_f = os.system(fr_main_to_res_f)
    if m_r_f == 0:
        x = f'{fr_main_to_res_f} && {checker}'
        x_x = os.system(x)
        if x_x == 0:
            calling_output = subprocess.check_output(x, shell=True)
            ss = calling_output.decode('cp866')
            z_z = r"\test\main\results"
            yy = f"{ld_1}:" + z_z
            if ss == yy:
                with open(results, 'a') as m_r_f_rep:
                    m_r_f_rep.write('Переход во вложенный каталог на 1 уровень успешен с указанием папки')
                break
    else:
        with open(results, 'a') as m_r_rep:
            m_r_rep.write('Баг! Переход во вложенный каталог на 1 уровень не осуществлен с указанием папки!')
        break
# Переход из main во вложенный каталог - result с помощью указания полного пути на 1 уровень
while True:
    fr_main_to_res_p = f'cd {ld_1}://test/main/results/'
    m_r_p = os.system(fr_main_to_res_p)
    if m_r_p == 0:
        x = f'{fr_main_to_res_p} && {checker}'
        x_x = os.system(x)
        if x_x == 0:
            calling_output = subprocess.check_output(x, shell=True)
            ss = calling_output.decode('cp866')
            z_z = r"\test\main\results"
            yy = f"{ld_1}:" + z_z
            if ss == yy:
                with open(results, 'a') as m_r_p_rep:
                    m_r_rep.write('Переход во вложенный каталог на 1 уровень успешен с указанием полного пути')
                break
    else:
        with open(results, 'a') as m_r_p_rep:
            m_r_rep.write('Баг! Переход во вложенный каталог на 1 уровень не осуществлен с указанием полного пути!')
        break

# переход из main во вложенный каталог - result с помощью указания вложенного пути - на 2 уровня вниз

# переход из main на 1 уровень вверх с помощью cd ..

# переход из main на 1 уровень вверх с помощью указания пути






# каллинг аутпут можно сделать функцией