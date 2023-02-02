#В последовательности на n целых элементов найти среднее арифметическое
#элементов первой трети
from functools import reduce
def calc_average(lst):
 return reduce(lambda a, b: a + b, lst) / len(lst)
lst = [24, 105, 35, 46, 75, 29, 30, 18, 4]
average = calc_average(lst[0:3])
print("среднее арифметическое 1/3: ", average)

