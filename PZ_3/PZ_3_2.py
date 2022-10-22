try:
    print('введите два целых числа A, B через пробел: ')
    A,B = map(int,input().split())
    if A != B:
        A1 = A+B
        B1 = A+B
        print('A = ', A1, 'B = ', B1)
    elif A == B:
        A = 0
        B = 0
        print('A = ', A, 'B = ', B)
except ValueError:
    print('ValueError')
