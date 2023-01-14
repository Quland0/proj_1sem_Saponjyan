# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Сумма элементов:
# Элементы до n-1 умножены на элемент n:

from random import randint
A = [randint(-100, 100) for i in range(10)]
B = "".join(map(str, A))
f1 = open('data_1.txt', 'w')
f1.writelines(str(A))
f1.close()

f2 = open('data_2.txt', 'w')
f2.write('Исходные данные: ')
f2.write('\n')
f2.writelines(A)
f2.close()

f1 = open('data_1.txt')
k = f1.read()
k = k.split()
for i in range(len(k)):
 k[i] = int(k[i])
f1.close()