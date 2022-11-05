#Дан список размера N и целые числа K и L (1 < K < L < N). Найти сумму элементов
#списка с номерами от K до L включительно.


N = int(input('введите размер списка: '))
K = int(input('введите K: '))
L = int(input('введите L: '))
list1 = []
w = 0
for i in range(N):
    list1.append(int(input()))
for i in range(K, L+1):
    w += list1[i]
print(w)
