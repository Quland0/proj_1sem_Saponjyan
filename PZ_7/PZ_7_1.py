#Дана строка. Если она представляет собой запись целого числа, то вывести 1, если
#вещественного (с дробной частью) — вывести 2; если строку нельзя преобразовать
#в число, то вывести 0. Считать, что дробная часть вещественного числа отделяется
#от его целой части десятичной точкой «.»
a = input('вводи: ')
try:
    a = int(a)
    print('1')
except ValueError:
    try:
        a = float(a)
        print('2')
    except ValueError:
        print('0')
