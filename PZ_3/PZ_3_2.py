try:
    print('введите два целых числа A, B через пробел: ')
    A,B = map(int,input().split())
    if A != B: #цикл, если A не равно В
        A1 = A+B
        B1 = A+B
        print('A = ', A1, 'B = ', B1) #вывод ответа
    elif A == B: #Цикл, если A не равно В
        A = 0
        B = 0
        print('A = ', A, 'B = ', B) #вывод ответа
except ValueError:
    print('ValueError')
