import random
l = [random.randint(-50, 50) for i in range(10)]
f = open("out.txt", "w")
f.write("Исходные данные:")
for i in l:
    f.write(" " + str(i))
f.write("\nКоличество элементов: " + str(len(l)))
f.write("\nСумма элементов: " + str(sum(l)))
f.write("\nЭлементы до n-1 умножены на элемент n:")
for i in l[:-1]:
    f.write(" " + str(i * l[-1]))
f.close()