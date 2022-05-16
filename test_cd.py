# Импортируем библиотеки
import os
import subprocess
import sys
import argparse
from datetime import datetime
from datetime import date
# Директории предварительно созданы. Ввод имен рабочих директорий:
while True:
    ld_1 = str.upper(str.strip(input('Введите наименование локального диска (на латиннице), где создана тестовая директория,\nявляющейся основной для тестирования - туда будет загружен результат тестирования\n в созданнную скриптом папку result\n')))
    ld_2 = str.upper(str.strip(input('Введите наименование другого диска (на латиннице), где создана побочная тестовая директория,\nнеобходимая для тестирования перехода между локальными дисками\n')))
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
# 1. Переход из main во вложенный каталог - result с помощью указания папки +
while True:
    fr_main_to_res_f = 'cd result'
    m_r_f = os.system(fr_main_to_res_f)
    if m_r_f == 0:
        with open(results, 'a') as m_r_f_rep:
            m_r_f_rep.write('Переход во вложенный каталог на 1 уровень успешен с указанием папки\n')
        break
    else:
        with open(results, 'a') as m_r_f_rep:
            m_r_f_rep.write('Баг! Переход во вложенный каталог на 1 уровень не осуществлен с указанием папки!\n')
        break
# 2. Переход из main во вложенный каталог - result с помощью указания полного пути на 1 уровень +
while True:
    fr_main_to_res_p_r = r'\test\main\results'
    fr_main_to_res_p = f'cd {ld_1}:' + fr_main_to_res_p_r
    m_r_p = os.system(fr_main_to_res_p)
    if m_r_p == 0:
        with open(results, 'a') as m_r_p_rep:
            m_r_p_rep.write('Переход во вложенный каталог на 1 уровень успешен с указанием полного пути')
        break
    else:
        with open(results, 'a') as m_r_p_rep:
            m_r_p_rep.write('Баг! Переход во вложенный каталог на 1 уровень не осуществлен с указанием полного пути!')
        break
# 3. Переход из main во вложенный каталог - 1 с помощью указания вложенного пути - на 2 уровня вниз
while True:
    fr_main_to_1_p = r'cd \results\1'
    m_1_p = os.system(fr_main_to_1_p)
    if m_1_p == 0:
        with open(results, 'a') as m_1_rep:
            m_1_rep.write('Переход во вложенный каталог на 2 уровня вниз успешен с указанием вложенного пути')
        break
    else:
        with open(results, 'a') as m_1_rep:
            m_1_rep.write('Баг! Переход во вложенный каталог на 2 уровня вниз не осуществлен с указанием вложенного пути!')
        break
# 4. Переход из main на 1 уровень вверх с помощью cd ..
while True:
    fr_main_to_up = 'cd ..'
    m_up = os.system(fr_main_to_up)
    if m_up == 0:
        with open(results, 'a') as m_up_rep:
            m_up_rep.write('Переход на 1 уровень вверх успешен с помощью cd ..')
        break
    else:
        with open(results, 'a') as m_up_rep:
            m_up_rep.write('Баг! Переход на 1 уровень вверх не осуществлен с помощью cd ..!')
        break
# 5. Переход из main на 1 уровень вверх с помощью указания полного пути
while True:
    fr_main_to_up_p_r = r'\test'
    fr_main_to_up_p = f'cd {ld_1}:' + fr_main_to_up_p_r
    m_up_p = os.system(fr_main_to_up_p)
    if m_up_p == 0:
        with open(results, 'a') as m_up_p_rep:
            m_up_p_rep.write('Переход на 1 уровень вверх успешен с указания полного пути')
        break
    else:
        with open(results, 'a') as m_up_p_rep:
            m_up_p_rep.write('Баг! Переход на 1 уровень вверх не осуществлен с указания полного пути!')
        break
# 6. Переход в корневой каталог
while True:
    fr_main_root = str.strip(r'cd\ ')
    m_r = os.system(fr_main_root)
    if m_r == 0:
        with open(results, 'a') as m_r_rep:
            m_r_rep.write(r'Переход в корень успешен с помощью команды cd\ ')
        break
    else:
        with open(results, 'a') as m_r_rep:
            m_r_rep.write(r'Баг! Переход в корень не осуществлен с помощью команды cd\!')
        break
# 7. Переход на другой диск на 2 уровня вниз с помощью /d
while True:
    fr_main_to_od_r = r'\test2\2'
    fr_main_to_od = f'cd /d {ld_2}:' + fr_main_to_od_r
    m_od = os.system(fr_main_to_od)
    if m_od == 0:
        with open(results, 'a') as m_w_d_rep:
            m_w_d_rep.write(r'Переход а другой диск на 2 уровня с помощью /d успешен')
        break
    else:
        with open(results, 'a') as m_w_d_rep:
            m_w_d_rep.write(r'Баг! Переход а другой диск на 2 уровня с помощью /d не осуществлен!')
        break
# 8. Попытка перехода с указанием /d но на этом же локальном диске
while True:
    fr_main_to_r_d_r = r'\test\main\results'
    fr_main_to_r_d = f'cd\ /d {ld_1}:' + fr_main_to_r_d_r
    m_w_d = os.system(fr_main_to_r_d)
    if m_w_d == 0:
        with open(results, 'a') as m_r_w_d_rep:
            m_r_w_d_rep.write(r'Переход перехода с указанием /d но на этом же локальном диске успешен')
        break
    else:
        with open(results, 'a') as m_r_w_d_rep:
            m_r_w_d_rep.write(r'Баг! Переход перехода с указанием /d но на этом же локальном диске не осуществлен!')
        break
# 9. Попытка перехода на другой диск без /d
while True:
    fr_main_to_r_wd_r = r'\test2\2'
    fr_main_to_r_wd = f'cd {ld_2}:' + fr_main_to_r_wd_r
    m_w_wd = os.system(fr_main_to_r_wd)
    if m_w_wd == 0:
        with open(results, 'a') as m_r_w_wd_rep:
            m_r_w_wd_rep.write(r'Попытка перехода на другой диск без /d не осуществлена')
        break
    else:
        with open(results, 'a') as m_r_w_wd_rep:
            m_r_w_wd_rep.write(r'Баг! Переход на другой диск без /d отработан некорректно!')
        break
# 10. Попытка перехода в несуществующие директории
error_1 = 'Системе не удается найти указанный путь.'
while True:
    fr_main_to_2 = r'cd \results\2'
    m_2_p = os.system(fr_main_to_2)
    if m_2_p == 1:
        output = subprocess.getoutput(m_2_p)
        o = output.encode('cp1251')
        o_o = (o.decode('cp866'))
        calling_output = subprocess.check_output('echo %cd%', shell=True)
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
# 11. Попытка перехода в папку с пробелами в названии с указанием полного пути:
while True:
    fr_main_to_lf_r = r'\test\main\results\last folder'
    fr_main_to_lf_p = f'cd {ld_1}:' + fr_main_to_res_p_r
    m_lf = os.system(fr_main_to_lf_p)
    if m_lf == 0:
        with open(results, 'a') as m_lf_rep:
            m_r_p_rep.write('Переход в папку с пробелом в названии с указанием полного пути успешен')
        break
    else:
        with open(results, 'a') as m_lf_rep:
            m_r_p_rep.write('Баг! Переход в папку с пробелом в названии с указанием полного пути не осуществлен!')
        break
# 12. Попытка перехода в папку с пробелами в названии с указанием полного пути и с использованием кавычек:
while True:
    fr_main_to_lf_r = r'\test\main\results\"last folder"'
    fr_main_to_lf_p = f'cd {ld_1}:' + fr_main_to_res_p_r
    m_lf = os.system(fr_main_to_lf_p)
    if m_lf == 0:
        with open(results, 'a') as m_lf_rep:
            m_r_p_rep.write('Переход в папку с пробелом в названии с указанием полного пути и кавычек успешен')
        break
    else:
        with open(results, 'a') as m_lf_rep:
            m_r_p_rep.write('Баг! Переход в папку с пробелом в названии с указанием полного пути и кавычек не осуществлен!')
        break
# 13. Переход на другой диск с использованием обратных слешей
while True:
    fr_main_to_od_r = r'/test2/2'
    fr_main_to_od = f'cd /d {ld_2}:' + fr_main_to_od_r
    m_od = os.system(fr_main_to_od)
    if m_od == 0:
        with open(results, 'a') as m_w_d_rep:
            m_w_d_rep.write(r'Переход на другой диск с использованием обратных слешей успешен')
        break
    else:
        with open(results, 'a') as m_w_d_rep:
            m_w_d_rep.write(r'Баг! ППереход на другой диск с использованием обратных слешей не осуществлен!')
        break
# 14. Переход на другой диск с использованием обратного слеша (\d)
while True:
    fr_main_to_od_r = r'\test2\2'
    fr_main_to_od = f'cd \d {ld_2}:' + fr_main_to_od_r
    m_od = os.system(fr_main_to_od)
    if m_od == 0:
        with open(results, 'a') as m_w_d_rep:
            m_w_d_rep.write(r'Переход а другой диск на 2 уровня с помощью /d успешен')
        break
    else:
        with open(results, 'a') as m_w_d_rep:
            m_w_d_rep.write(r'Баг! Переход а другой диск на 2 уровня с помощью /d не осуществлен!')
        break
# 15. Переход из main во вложенный каталог - result с помощью указания полного пути на 1 уровень с использованием двойных слешей
while True:
    fr_main_to_res_p_r = r'\\test\\main\\results'
    print(fr_main_to_res_p_r)
    fr_main_to_res_p = f'cd {ld_1}:' + fr_main_to_res_p_r
    m_r_p = os.system(fr_main_to_res_p)
    if m_r_p == 0:
        with open(results, 'a') as m_r_p_rep:
            m_r_p_rep.write('Переход во вложенный каталог на 1 уровень успешен с указанием полного пути и двойных слешей')
        break
    else:
        with open(results, 'a') as m_r_p_rep:
            m_r_p_rep.write('Баг! Переход во вложенный каталог на 1 уровень не осуществлен с указанием полного пути и двойных слешей!')
        break
# 16. Переход из main во вложенный каталог - result с помощью указания полного пути на 1 уровень с использованием двойных и одинарных слешей
while True:
    fr_main_to_res_p_r = r'\\test\main\results'
    print(fr_main_to_res_p_r)
    fr_main_to_res_p = f'cd {ld_1}:' + fr_main_to_res_p_r
    m_r_p = os.system(fr_main_to_res_p)
    if m_r_p == 0:
        with open(results, 'a') as m_r_p_rep:
            m_r_p_rep.write('Переход во вложенный каталог на 1 уровень успешен с указанием полного пути и двойных, и одинарных слешей')
        break
    else:
        with open(results, 'a') as m_r_p_rep:
            m_r_p_rep.write('Баг! Переход во вложенный каталог на 1 уровень не осуществлен с указанием полного пути и двойных, и одинарных слешей!')
        break
# 17. Попытка перехода в скрытую папку c указанием полного пути
while True:
    fr_main_to_res_p_r = r'\test\main\results\hidden'
    fr_main_to_res_p = f'cd {ld_1}:' + fr_main_to_res_p_r
    m_r_p = os.system(fr_main_to_res_p)
    if m_r_p == 0:
        with open(results, 'a') as m_r_p_rep:
            m_r_p_rep.write('Попытка перехода в скрытую папку c указанием полного пути успешна')
        break
    else:
        with open(results, 'a') as m_r_p_rep:
            m_r_p_rep.write('Баг! Переход в скрытую папку c указанием полного пути не осуществлена!')
        break
# 18. Переход в директорию, содержащую имя на кириллице с указанием полного пути:
while True:
    fr_main_to_res_p_r = r'\test\main\results\кириллица'
    fr_main_to_res_p = f'cd {ld_1}:' + fr_main_to_res_p_r
    m_r_p = os.system(fr_main_to_res_p)
    if m_r_p == 0:
        with open(results, 'a') as m_r_p_rep:
            m_r_p_rep.write('Попытка перехода в директорию, содержащую имя на кириллице с указанием полного пути успешна')
        break
    else:
        with open(results, 'a') as m_r_p_rep:
            m_r_p_rep.write('Баг! Переход в директорию, содержащую имя на кириллице с указанием полного пути не осуществлена!')
        break
# 19. Переход в директорию, содержащую имя на латиннице в разных регистрах с несоблюдением регистра:
while True:
    fr_main_to_res_p_r = r'\test\main\results\rEg'
    fr_main_to_res_p = f'cd {ld_1}:' + fr_main_to_res_p_r
    m_r_p = os.system(fr_main_to_res_p)
    if m_r_p == 0:
        with open(results, 'a') as m_r_p_rep:
            m_r_p_rep.write('Переход в директорию, содержащую имя на латиннице в разных регистрах с несоблюдением регистра успешна')
        break
    else:
        with open(results, 'a') as m_r_p_rep:
            m_r_p_rep.write('Баг! Переход в директорию, содержащую имя на латиннице в разных регистрах с несоблюдением регистра не осуществлена!')
        break
# 20. Переход в директорию, содержащую имя на латиннице, кириллице и с испольщованием цифр, иных символов:
while True:
    fr_main_to_res_p_r = r'\test\main\results\lat1кир$'
    fr_main_to_res_p = f'cd {ld_1}:' + fr_main_to_res_p_r
    m_r_p = os.system(fr_main_to_res_p)
    if m_r_p == 0:
        with open(results, 'a') as m_r_p_rep:
            m_r_p_rep.write('Переход в директорию, содержащую имя на латиннице, кириллице и с испольщованием цифр, иных символов успешен')
        break
    else:
        with open(results, 'a') as m_r_p_rep:
            m_r_p_rep.write('Баг! Переход в директорию, содержащую имя на латиннице, кириллице и с испольщованием цифр, иных символов не осуществлена!')
        break
# 21. Использование нижнего регистра при указании локального диска для перехода (ранее - в верхнем)
while True:
    fr_main_to_res_p_r = r'\test\main\results'
    ld_3 = str.lower(ld_1)
    fr_main_to_res_p = f'cd {ld_3}:' + fr_main_to_res_p_r
    m_r_p = os.system(fr_main_to_res_p)
    if m_r_p == 0:
        with open(results, 'a') as m_r_p_rep:
            m_r_p_rep.write('Использование нижнего регистра при указании локального диска для перехода успешно')
        break
    else:
        with open(results, 'a') as m_r_p_rep:
            m_r_p_rep.write('Баг! Использование нижнего регистра при указании локального диска для перехода не осуществлено!')
        break