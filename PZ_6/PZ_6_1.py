#Дан список размера N и целые числа K и L (1 < K < L < N). Найти сумму элементов
#списка с номерами от K до L включительно
import random


N = int(input("Введите кол-во элементов массива: "))
lst = [random.randint(1, 100) for _ in range(N)]

print(f"Список {lst}")

K = int(input("Введите K: "))
L = int(input("Введите L: "))

sum_ = 0
for i in range(K, L+1):
    sum_ += lst[i]

print(f"Сумма элементов с {K} по {L} позиции = {sum_}")