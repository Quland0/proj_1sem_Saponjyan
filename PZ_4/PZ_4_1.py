#Дано вещественное число X и целое число N (> 0). Найти значение выражения
# X -X3/(3!) + X5/(5!) - ... + (-1)N-X2-N+1/((2-N+1)!) (N! = 12 ...N). Полученное число
#является приближенным значением функции sin в точке X.

x = float(input('х = ')) #принимаем вещественное число в переменную
n = int(input('n = ')) #принимаем целое число в переменную
p = x
s = x
k = 0
for i in range(1, n+1): #тело цикла
    k += 2
    p *= (-1) * x * x / (k * (k + 1))
    s += p
print(s) #вывод результата