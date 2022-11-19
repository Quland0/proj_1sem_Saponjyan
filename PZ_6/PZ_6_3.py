#Дан список размера N, все элементы которого, кроме последнего, упорядочены по
#возрастанию. Сделать список упорядоченным, переместив последний элемент на
#новую позицию.


import random


N = int(input("Введите кол-во элементов массива: "))

lst = [random.randint(50, 100) for _ in range(N-1)]
lst.sort()
lst.append(random.randint(1, 50))

print(lst)

pos = int(input("Введите позицию куда вы хотите переместить последний элемент: "))
el = lst.pop(-1)

lst.insert(pos, el)
print(lst)