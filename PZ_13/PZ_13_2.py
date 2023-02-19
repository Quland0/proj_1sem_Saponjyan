#Перенести в новую матрицу Matr1 элементы, которые не находятся в первых и
#последних сроках и столбцах матрицы Matr2 произвольного размера.
import random
n = int(input("Введите размер матрицы: ")) # Записываем размер матрицы
sourceMatrix = [[random.randint(0, 10) for i in range(n)] for j in range(n)]
print("\nИсходная матрица: ")
for row in sourceMatrix:
    print(row)
newMatrix = [[0 for i in range(n-2)] for j in range(n - 2)]
for i in range(1, n - 1):
    for j in range(1, n - 1):
        newMatrix[i - 1][j - 1] = sourceMatrix[i][j]
print("\nВыходная матрица: ")
for row in newMatrix:
    print(row)