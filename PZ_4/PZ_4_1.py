x = float(input('х = '))
n = int(input('n = '))
p = x
s = x
k = 0
for i in range(1, n+1):
    k += 2
    p *= (-1) * x * x / (k * (k + 1))
    s += p
print(s)