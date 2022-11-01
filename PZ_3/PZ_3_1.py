 #Проверить истинность высказывания: «Среди трех данных целых чисел есть хотя бы
#одна пара совпадающих».
try:
    print('введите 3 целых числа через пробел: ') #запрос на 3 целых чисел
    a,b,c = map(int,input().split()) #принимаем числа в переменные

    if a==b or a==c or b==c:
        print('true')
    else:
        print('false')
except ValueError:
    print('ValueError')
