n = int(input('n = '))
s = 0.0
p = n
for i in range(1, n + 1):
    s += 1.0 / i ** p
print(s)
