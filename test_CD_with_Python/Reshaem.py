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
r.write('Результаты тестирования команды CD:')
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
        with open(results, 'a') as m_r_f_rep:
            m_r_f_rep.write('Баг! Переход во вложенный каталог на 1 уровень не осуществлен с указанием папки!')
        break
# Переход из main во вложенный каталог - result с помощью указания полного пути на 1 уровень
while True:
    fr_main_to_res_p_r = r'\test\main\results'
    fr_main_to_res_p = f'cd {ld_1}:' + fr_main_to_res_p_r
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
                    m_r_p_rep.write('Переход во вложенный каталог на 1 уровень успешен с указанием полного пути')
                break
    else:
        with open(results, 'a') as m_r_p_rep:
            m_r_p_rep.write('Баг! Переход во вложенный каталог на 1 уровень не осуществлен с указанием полного пути!')
        break

# переход из main во вложенный каталог - 1 с помощью указания вложенного пути - на 2 уровня вниз
while True:
    fr_main_to_1_p = r'cd \results\1'
    m_1_p = os.system(fr_main_to_1_p)
    if m_1_p == 0:
        x = f'{fr_main_to_1_p} && {checker}'
        x_x = os.system(x)
        if x_x == 0:
            calling_output = subprocess.check_output(x, shell=True)
            ss = calling_output.decode('cp866')
            z_z = r"\test\main\results\1"
            yy = f"{ld_1}:" + z_z
            if ss == yy:
                with open(results, 'a') as m_1_rep:
                    m_1_rep.write('Переход во вложенный каталог на 2 уровня вниз успешен с указанием вложенного пути')
                break
    else:
        with open(results, 'a') as m_1_rep:
            m_1_rep.write('Баг! Переход во вложенный каталог на 2 уровня вниз не осуществлен с указанием вложенного пути!')
        break
# Переход из main на 1 уровень вверх с помощью cd ..
while True:
    fr_main_to_up = 'cd ..'
    m_up = os.system(fr_main_to_up)
    if m_up == 0:
        x = f'{fr_main_to_up} && {checker}'
        x_x = os.system(x)
        if x_x == 0:
            calling_output = subprocess.check_output(x, shell=True)
            ss = calling_output.decode('cp866')
            z_z = r"\test"
            yy = f"{ld_1}:" + z_z
            if ss == yy:
                with open(results, 'a') as m_up_rep:
                    m_up_rep.write('Переход на 1 уровень вверх успешен с помощью cd ..')
                break
    else:
        with open(results, 'a') as m_up_rep:
            m_up_rep.write('Баг! Переход на 1 уровень вверх не осуществлен с помощью cd ..!')
        break
# переход из main на 1 уровень вверх с помощью указания полного пути
while True:
    fr_main_to_up_p_r = r'\test'
    fr_main_to_up_p = f'cd {ld_1}:' + fr_main_to_up_p_r
    m_up_p = os.system(fr_main_to_up_p)
    if m_up_p == 0:
        x = f'{fr_main_to_up_p} && {checker}'
        x_x = os.system(x)
        if x_x == 0:
            calling_output = subprocess.check_output(x, shell=True)
            ss = calling_output.decode('cp866')
            z_z = r"\test"
            yy = f"{ld_1}:" + z_z
            if ss == yy:
                with open(results, 'a') as m_up_p_rep:
                    m_up_p_rep.write('Переход на 1 уровень вверх успешен с указания полного пути')
                break
    else:
        with open(results, 'a') as m_up_p_rep:
            m_up_p_rep.write('Баг! Переход на 1 уровень вверх не осуществлен с указания полного пути!')
        break
# Переход в корневой каталог
while True:
    fr_main_root = str.strip(r'cd\ ')
    m_r = os.system(fr_main_root)
    if m_r == 0:
        x = f'{fr_main_root} && {checker}'
        x_x = os.system(x)
        if x_x == 0:
            calling_output = subprocess.check_output(x, shell=True)
            ss = calling_output.decode('cp866')
            z_z = str.strip(r'\ ')
            yy = f"{ld_1}:" + z_z
            if ss == yy:
                with open(results, 'a') as m_r_rep:
                    m_r_rep.write(r'Переход в корень успешен с помощью команды cd\ ')
                break
    else:
        with open(results, 'a') as m_r_rep:
            m_r_rep.write(r'Баг! Переход в корень не осуществлен с помощью команды cd\!')
        break
# Переход на другой диск на 2 уровня с помощью /d
while True:
    fr_main_to_od_r = r'\test2\2'
    fr_main_to_od = f'cd\ /d {ld_2}:' + fr_main_to_od_r
    m_od = os.system(fr_main_to_od)
    if m_od == 0:
        x = f'{fr_main_to_od} && {checker}'
        x_x = os.system(x)
        if x_x == 0:
            calling_output = subprocess.check_output(x, shell=True)
            ss = calling_output.decode('cp866')
            z_z = r'\test2\2'
            yy = f"{ld_2}:" + z_z
            if ss == yy:
                with open(results, 'a') as m_w_d_rep:
                    m_w_d_rep.write(r'Переход а другой диск на 2 уровня с помощью \d успешен')
                break
    else:
        with open(results, 'a') as m_w_d_rep:
            m_w_d_rep.write(r'Баг! Переход а другой диск на 2 уровня с помощью \d не осуществлен!')
        break
# Попытка перехода с указанием /d но на этом же локальном диске
while True:
    fr_main_to_r_d_r = r'\test\main\results'
    fr_main_to_r_d = f'cd\ /d {ld_1}:' + fr_main_to_r_d_r
    m_w_d = os.system(fr_main_to_r_d)
    if m_w_d == 0:
        x = f'{fr_main_to_r_d} && {checker}'
        x_x = os.system(x)
        if x_x == 0:
            calling_output = subprocess.check_output(x, shell=True)
            ss = calling_output.decode('cp866')
            z_z = r'\test\main\results'
            yy = f"{ld_1}:" + z_z
            if ss == yy:
                with open(results, 'a') as m_r_w_d_rep:
                    m_r_w_d_rep.write(r'Переход перехода с указанием /d но на этом же локальном диске успешен')
                break
    else:
        with open(results, 'a') as m_r_w_d_rep:
            m_r_w_d_rep.write(r'Баг! Переход перехода с указанием /d но на этом же локальном диске не осуществлен!')
        break
# Попытка перехода на другой диск без /d
while True:
    fr_main_to_r_wd_r = r'\test2\2'
    fr_main_to_r_wd = f'cd\ {ld_2}:' + fr_main_to_r_d_r
    m_w_wd = os.system(fr_main_to_r_wd)
    if m_w_wd == 0:
        x = f'{fr_main_to_r_wd} && {checker}'
        x_x = os.system(x)
        if x_x == 0:
            calling_output = subprocess.check_output(x, shell=True)
            ss = calling_output.decode('cp866')
            z_z = r'\test\main'
            yy = f"{ld_1}:" + z_z
            if ss == yy:
                with open(results, 'a') as m_r_w_wd_rep:
                    m_r_w_wd_rep.write(r'Попытка перехода на другой диск без /d не осуществлена')
                break
    else:
        with open(results, 'a') as m_r_w_wd_rep:
            m_r_w_wd_rep.write(r'Баг! Переход на другой диск без /d осуществлен!')
        break
# Попытка перехода в несуществующие директории
error_1 = 'Системе не удается найти указанный путь.'
while True:
    fr_main_to_2 = r'cd \results\2'
    m_2_p = os.system(fr_main_to_2)
    if m_2_p == 1:
        output = subprocess.getoutput(m_2_p)
        o = output.encode('cp1251')
        o_o = (o.decode('cp866'))
        calling_output = subprocess.check_output(checker, shell=True)
        ss = calling_output.decode('cp866')
        z_z = r'\test\main'
        yy = f'{ld_1}' + z_z
        if ss == yy:
            if o_o == error_1:
                with open(results, 'a') as m_2_rep:
                    m_2_rep.write('Ошибка перехода отработа верно. Текст ошибки релевантен')
                break
    else:
        with open(results, 'a') as m_2_rep:
            m_2_rep.write('Баг! Ошибка перехода отработа неверно. Текст ошибки нерелевантен!')
        break
# Переход в папки, названия которых содержат пробелы, но без кавычек

# Переход в папки, названия которых содержат пробелы, но с кавычками



# каллинг аутпут можно сделать функцией