# Импортируем библиотеки
import os
import subprocess
from datetime import date
# Директории предварительно созданы. Ввод имен рабочих директорий:
while True:
    ld_1 = str.upper(str.strip(input('Введите наименование локального диска (на латиннице), где создана тестовая директория,\nявляющейся основной, где также будут результаты:\n')))
    ld_2 = str.upper(str.strip(input('Введите наименование другого диска (на латиннице), где создана побочная тестовая директория,\nнеобходимая для тестирования перехода между локальными дисками:\n')))
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
r.write('Результаты тестирования команды CD:\n')
r.close()
# Начинаем тестирование из предварительно настроенной стартовой директории (main). Справочно: Переход = Изменение директории
# 1. Переход из main во вложенный каталог - result с помощью указания папки (+)
while True:
    fr_main_to_res_f = 'cd results'
    m_r_f = os.system(fr_main_to_res_f)
    if m_r_f == 0:
        with open(results, 'a') as m_r_f_rep:
            m_r_f_rep.write('1. Успех. Переход во вложенный каталог на 1 уровень глубины успешен с указанием имени папки\n')
        break
    else:
        with open(results, 'a') as m_r_f_rep:
            m_r_f_rep.write('1. Баг! Переход во вложенный каталог на 1 уровень глубины не осуществлен с указанием имени вложенной папки!\n')
        break
# 2. Переход из main во вложенный каталог - result с помощью указания полного пути на 1 уровень глубины +
while True:
    fr_main_to_res_p_r = r'\test\main\results'
    fr_main_to_res_p = f'cd {ld_1}:' + fr_main_to_res_p_r
    m_r_p = os.system(fr_main_to_res_p)
    if m_r_p == 0:
        with open(results, 'a') as m_r_p_rep:
            m_r_p_rep.write('2. Успех. Переход во вложенный каталог на 1 уровень глубины успешен с указанием полного пути\n')
        break
    else:
        with open(results, 'a') as m_r_p_rep:
            m_r_p_rep.write('2. Баг! Переход во вложенный каталог на 1 уровень глубины не осуществлен с указанием полного пути\n!')
        break
# 3. Переход из main во вложенный каталог "1" с помощью указания вложенного пути - на 2 уровня глубины
while True:
    fr_main_to_1_p = r'cd results\1'
    m_1_p = os.system(fr_main_to_1_p)
    if m_1_p == 0:
        with open(results, 'a') as m_1_rep:
            m_1_rep.write('3. Успех. Переход во вложенный каталог на 2 уровня глубины успешен с указанием вложенного пути\n')
        break
    else:
        with open(results, 'a') as m_1_rep:
            m_1_rep.write('3. Баг! Переход во вложенный каталог на 2 уровня глубины не осуществлен с указанием вложенного пути\n!')
        break
# 4. Переход из main на 1 уровень вверх с помощью cd.. (слитно)
while True:
    fr_main_to_up = 'cd..'
    m_up = os.system(fr_main_to_up)
    if m_up == 0:
        with open(results, 'a') as m_up_rep:
            m_up_rep.write('4. Успех. Переход в родительский каталог 1 уровень вверх успешен с помощью команды "cd.." (слитно)\n')
        break
    else:
        with open(results, 'a') as m_up_rep:
            m_up_rep.write('4. Баг! Переход в родительский каталог на 1 уровень вверх не осуществлен с помощью "cd.." (слитно)\n!')
        break
# 5. Переход из main на 1 уровень вверх с помощью cd .. (раздельно)
while True:
    fr_main_to_up_c = 'cd ..'
    m_up_c = os.system(fr_main_to_up_c)
    if m_up_c == 0:
        with open(results, 'a') as m_up_c_rep:
            m_up_c_rep.write('5. Успех. Переход в родительский каталог 1 уровень вверх успешен с помощью команды "cd .." (раздельно)\n')
        break
    else:
        with open(results, 'a') as m_up_c_rep:
            m_up_c_rep.write('5. Баг! Переход в родительский каталог на 1 уровень вверх не осуществлен с помощью "cd .." (раздельно)\n!')
        break
# 6. Переход из main на 1 уровень вверх (в родительский каталог) с помощью указания полного пути
while True:
    fr_main_to_up_p_r = r'\test'
    fr_main_to_up_p = f'cd {ld_1}:' + fr_main_to_up_p_r
    m_up_p = os.system(fr_main_to_up_p)
    if m_up_p == 0:
        with open(results, 'a') as m_up_p_rep:
            m_up_p_rep.write('6. Успех. Переход на 1 уровень вверх (в род. каталог) успешен с указанием полного пути\n')
        break
    else:
        with open(results, 'a') as m_up_p_rep:
            m_up_p_rep.write('6. Баг! Переход на 1 уровень вверх (в род. каталог) не осуществлен с указанием полного пути!\n')
        break
# 7. Переход в корневой каталог с помощью команды "cd\"
while True:
    fr_main_root = str.strip(r'cd\ ')
    m_r = os.system(fr_main_root)
    if m_r == 0:
        with open(results, 'a') as m_r_rep:
            m_r_rep.write(r'7. Успех. Переход в корень успешен с помощью команды cd\ ' + '\n')
        break
    else:
        with open(results, 'a') as m_r_rep:
            m_r_rep.write(r'7. Баг! Переход в корень не осуществлен с помощью команды cd\!'  + '\n')
        break
# 8. Переход в корневой каталог с помощью команды "cd/"
while True:
    fr_main_root_sl = 'cd/'
    m_r_s = os.system(fr_main_root_sl)
    if m_r_s == 0:
        with open(results, 'a') as m_r_s_rep:
            m_r_s_rep.write('8. Успех. Переход в корень успешен с помощью команды cd/\n')
        break
    else:
        with open(results, 'a') as m_r_s_rep:
            m_r_s_rep.write('8. Баг! Переход в корень не осуществлен с помощью команды cd/!\n')
        break
# 9. Переход на другой диск на 2 уровня вниз с помощью /d
while True:
    fr_main_to_od_r = r'\test2\2'
    fr_main_to_od = f'cd /d {ld_2}:' + fr_main_to_od_r
    m_od = os.system(fr_main_to_od)
    if m_od == 0:
        with open(results, 'a') as m_w_d_rep:
            m_w_d_rep.write('9. Успех. Переход на другой диск с помощью /d успешен\n')
        break
    else:
        with open(results, 'a') as m_w_d_rep:
            m_w_d_rep.write('9. Баг! Переход а другой диск на 2 уровня с помощью /d не осуществлен!\n')
        break
# 10. Попытка перехода на другой диск с обратным слешем указателя смены диска \d
error_1 = 'Синтаксическая ошибка в имени файла, имени папки или метке тома.'
while True:
    fr_main_to_od_w_r = r'\test2\2'
    fr_main_to_od_w = f'cd \d {ld_2}:' + fr_main_to_od_w_r
    m_od_w = os.system(fr_main_to_od_w)
    if m_od_w == 1:
        output_j = subprocess.getoutput(fr_main_to_od_w)
        j = output_j.encode('cp1251')
        j_j = (j.decode('cp866'))
        calling_output_j = subprocess.check_output('echo %cd%', shell=True)
        zz = calling_output_j.decode('cp866')
        zzz = zz.rstrip()
        t_t = r'\test\main'
        tt = f'{ld_1}:' + t_t
        if zzz == tt:
            if j_j == error_1:
                with open(results, 'a') as m_od_w_rep:
                    m_od_w_rep.write('10. Успех. Переход на другой диск с помощью \d не осуществлен. Текст ошибки верен\n')
                break
    else:
        with open(results, 'a') as m_od_w_rep:
            m_od_w_rep.write('10. Баг! Переход на другой диск с помощью \d отработан некорректно или текст ошибки не верен!\n')
        break
# 11. Попытка перехода с указанием /d, но в директорию на этом же (стартовом) локальном диске
while True:
    fr_main_to_r_d_r = r'\test\main\results'
    fr_main_to_r_d = f'cd /d {ld_1}:' + fr_main_to_r_d_r
    m_w_d = os.system(fr_main_to_r_d)
    if m_w_d == 0:
        with open(results, 'a') as m_w_d_rep:
            m_w_d_rep.write(r'11. Успех. Переход с указанием /d, но в директорию на текущем локальном диске успешен' + '\n')
        break
    else:
        with open(results, 'a') as m_w_d_rep:
            m_w_d_rep.write(r'11. Баг! Переход с указанием /d, но в директорию на текущем локальном диске не осуществлен!' + '\n')
        break
# 12. Попытка перехода на другой диск без /d
while True:
    fr_main_to_r_wd_r = r'\test2\2'
    fr_main_to_r_wd = f'cd {ld_2}:' + fr_main_to_r_wd_r
    m_w_wd = os.system(fr_main_to_r_wd)
    if m_w_wd == 0:
        with open(results, 'a') as m_w_wd_rep:
            m_w_wd_rep.write(r'12. Успех. Попытка перехода на другой диск без /d не осуществлена'+ '\n')
        break
    else:
        with open(results, 'a') as m_w_wd_rep:
            m_w_wd_rep.write(r'12. Баг! Переход на другой диск без /d отработан некорректно!'+ '\n')
        break
# 13. Попытка перехода в несуществующие директории
error_2 = 'Системе не удается найти указанный путь.'
while True:
    fr_main_to_2 = r'cd \results\2'
    m_2_p = os.system(fr_main_to_2)
    if m_2_p == 1:
        output_s = subprocess.getoutput(fr_main_to_2)
        o = output_s.encode('cp1251')
        o_o = (o.decode('cp866'))
        calling_output_s = subprocess.check_output('echo %cd%', shell=True)
        ss = calling_output_s.decode('cp866')
        sss = ss.rstrip()
        z_z = r'\test\main'
        yy = f'{ld_1}:' + z_z
        if sss == yy:
            if o_o == error_2:
                with open(results, 'a') as m_2_rep:
                    m_2_rep.write('13. Успех. Ошибка перехода отработа верно. Текст ошибки релевантен\n')
                break
    else:
        with open(results, 'a') as m_2_rep:
            m_2_rep.write('13. Баг! Ошибка перехода отработа неверно. Текст ошибки нерелевантен!\n')
        break
# 14. Попытка перехода в папку с пробелами в названии с указанием полного пути без кавычек:
while True:
    fr_main_to_lf_r = r'\test\main\results\1\last folder'
    fr_main_to_lf_p = f'cd {ld_1}:' + fr_main_to_lf_r
    m_lf = os.system(fr_main_to_lf_p)
    if m_lf == 0:
        with open(results, 'a') as m_lf_rep:
            m_lf_rep.write('14. Успех. Переход в папку с пробелом в названии с указанием полного пути без кавычек успешен\n')
        break
    else:
        with open(results, 'a') as m_lf_rep:
            m_lf_rep.write('14. Баг! Переход в папку с пробелом в названии с указанием полного пути без кавычек не осуществлен!\n')
        break
# 15. Попытка перехода в папку с пробелами в названии с указанием полного пути и с использованием кавычек:
while True:
    fr_main_to_lf_w_r = r'\test\main\results\1\"last folder"'
    fr_main_to_lf_w_p = f'cd {ld_1}:' + fr_main_to_lf_w_r
    m_lf_w = os.system(fr_main_to_lf_w_p)
    if m_lf_w == 0:
        with open(results, 'a') as m_lf_w_rep:
            m_lf_w_rep.write('15. Успех. Переход в папку с пробелом в названии с указанием полного пути и кавычек успешен\n')
        break
    else:
        with open(results, 'a') as m_lf_w_rep:
            m_lf_w_rep.write('15. Баг! Переход в папку с пробелом в названии с указанием полного пути и кавычек не осуществлен!\n')
        break
# 16. Переход на другой диск с использованием обратных слешей
while True:
    fr_main_to_od_rev_r = r'/test2/2'
    fr_main_to_od_rev = f'cd /d {ld_2}:' + fr_main_to_od_rev_r
    m_od_rev = os.system(fr_main_to_od_rev)
    if m_od_rev == 0:
        with open(results, 'a') as m_od_rev_rep:
            m_od_rev_rep.write('16. Успех. Переход на другой диск с использованием обратных слешей в пути успешен\n')
        break
    else:
        with open(results, 'a') as m_od_rev_rep:
            m_od_rev_rep.write('16. Баг! Переход на другой диск с использованием обратных слешей в пути не осуществлен!\n')
        break
# 17. Переход из main во вложенный каталог - result с помощью указания полного пути на 1 уровень с использованием двойных слешей
while True:
    fr_main_to_res_p2_r = r'\\test\\main\\results'
    fr_main_to_res_p2 = f'cd {ld_1}:' + fr_main_to_res_p2_r
    m_r_p2 = os.system(fr_main_to_res_p2)
    if m_r_p2 == 0:
        with open(results, 'a') as m_r_p2_rep:
            m_r_p2_rep.write('17. Успех. Переход во вложенный каталог на 1 уровень успешен с указанием полного пути и двойных слешей\n')
        break
    else:
        with open(results, 'a') as m_r_p2_rep:
            m_r_p2_rep.write('17. Баг! Переход во вложенный каталог на 1 уровень не осуществлен с указанием полного пути и двойных слешей!\n')
        break
# 18. Переход из main во вложенный каталог - result с помощью указания полного пути на 1 уровень с использованием двойных и одинарных слешей
while True:
    fr_main_to_res_pv_r = r'\\test\main\results'
    fr_main_to_res_pv = f'cd {ld_1}:' + fr_main_to_res_pv_r
    m_r_pv = os.system(fr_main_to_res_pv)
    if m_r_pv == 0:
        with open(results, 'a') as m_r_pv_rep:
            m_r_pv_rep.write('18. Успех. Переход во вложенный каталог на 1 уровень успешен с указанием полного пути и двойных, и одинарных слешей\n')
        break
    else:
        with open(results, 'a') as m_r_pv_rep:
            m_r_pv_rep.write('18. Баг! Переход во вложенный каталог на 1 уровень не осуществлен с указанием полного пути и двойных, и одинарных слешей!\n')
        break
# 19. Попытка перехода в скрытую папку c указанием полного пути
while True:
    fr_main_to_res_ph_r = r'\test\main\results\hidden'
    fr_main_to_res_ph = f'cd {ld_1}:' + fr_main_to_res_ph_r
    m_r_ph = os.system(fr_main_to_res_ph)
    if m_r_ph == 0:
        with open(results, 'a') as m_r_ph_rep:
            m_r_ph_rep.write('19. Успех. Переход в скрытую папку c указанием полного пути успешен\n')
        break
    else:
        with open(results, 'a') as m_r_ph_rep:
            m_r_ph_rep.write('19.Баг! Переход в скрытую папку c указанием полного пути не осуществлен!\n')
        break
# 20. Переход в директорию, содержащую имя на кириллице с указанием полного пути:
while True:
    fr_main_to_res_pk_r = r'\test\main\results\кириллица'
    fr_main_to_res_pk = f'cd {ld_1}:' + fr_main_to_res_pk_r
    m_r_pk = os.system(fr_main_to_res_pk)
    if m_r_pk == 0:
        with open(results, 'a') as m_r_pk_rep:
            m_r_pk_rep.write('20. Успех. Переход в директорию, содержащую имя на кириллице с указанием полного пути успешен\n')
        break
    else:
        with open(results, 'a') as m_r_pk_rep:
            m_r_pk_rep.write('20. Баг! Переход в директорию, содержащую имя на кириллице с указанием полного пути не осуществлен!\n')
        break
# 21. Переход в директорию, содержащую имя на латиннице в разных регистрах с несоблюдением регистра:
while True:
    fr_main_to_res_preg_r = r'\test\main\results\rEg'
    fr_main_to_res_preg = f'cd {ld_1}:' + fr_main_to_res_preg_r
    m_r_preg = os.system(fr_main_to_res_preg)
    if m_r_preg == 0:
        with open(results, 'a') as m_r_preg_rep:
            m_r_preg_rep.write('21. Успех. Переход в директорию, содержащую имя на латиннице в разных регистрах с несоблюдением регистра успешен\n')
        break
    else:
        with open(results, 'a') as m_r_preg_rep:
            m_r_preg_rep.write('21. Баг! Переход в директорию, содержащую имя на латиннице в разных регистрах с несоблюдением регистра не осуществлен!\n')
        break
# 22. Переход в директорию, содержащую имя на латиннице, кириллице, цифры, иные символы:
while True:
    fr_main_to_res_poth_r = r'\test\main\results\lat1кир$'
    fr_main_to_res_poth = f'cd {ld_1}:' + fr_main_to_res_poth_r
    m_r_poth = os.system(fr_main_to_res_poth)
    if m_r_poth == 0:
        with open(results, 'a') as m_r_poth_rep:
            m_r_poth_rep.write('22. Успех. Переход в директорию, содержащую имя на латиннице, кириллице, цифры, иные символы, успешен\n')
        break
    else:
        with open(results, 'a') as m_r_poth_rep:
            m_r_poth_rep.write('22. Баг! Переход в директорию, содержащую имя на латиннице, кириллице, цифры, иные символы, не осуществлен!\n')
        break
# 23. Использование нижнего регистра при указании локального диска для перехода (ранее - в верхнем)
while True:
    fr_main_to_res_p_low_r = r'\test\main\results'
    ld_3 = str.lower(ld_1)
    fr_main_to_res_plow = f'cd {ld_3}:' + fr_main_to_res_p_low_r
    m_r_plow = os.system(fr_main_to_res_plow)
    if m_r_plow == 0:
        with open(results, 'a') as m_r_plow_rep:
            m_r_plow_rep.write('23. Успех. Переход с указанием именем локального лиска в нижнем регистре успешен\n')
        break
    else:
        with open(results, 'a') as m_r_plow_rep:
            m_r_plow_rep.write('23. Баг! Переход с указанием именем локального лиска в нижнем регистре не осуществлен!\n')
        break
print('ТЕСТИРОВАНИЕ ЗАВЕРШЕНО. Результаты в текстовом документе в test/main/results')