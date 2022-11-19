#Дан целочисленный список размера N. Найти количество различных элементов в
#данном списке

import random
from collections import Counter


N = int(input("Введите кол-во элементов массива: "))
lst = [random.randint(1, 100) for _ in range(N)]
print(lst)

cnt = Counter(lst)

for key, value in cnt.items():
    print(f"Число {key} кол-во вхождений в список {value}")