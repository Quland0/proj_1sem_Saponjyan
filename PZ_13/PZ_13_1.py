#В матрице найти среднее арифметическое элементов последних двух столбцов.

from random import randint

org_matr = int(input('размер матрицы: '))
matrix = [[randint(0, 50) for i in range(org_matr)] for j in range(org_matr)]
print("\nИсходная матрица: ")
for i in matrix:
    print(*i, sep='\t' * 2)
arr = []
stolb_1 = org_matr - 1
stolb_2 = org_matr - 2
for item in range(0, len(matrix)):
    arr.append(matrix[item][stolb_1])
    arr.append(matrix[item][stolb_2])
summa = sum(arr)
print(f"среднее арифметическое последних двух столбцов: {summa / len(arr)}")