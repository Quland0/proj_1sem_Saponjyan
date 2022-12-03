#Организовать словарь avto, содержащий 3 ключа (марки авто) и списки
#из трех моделей в качестве значений. Обеспечить отображение вторых моделей по
#каждому авто, всех моделей словаря.

list_lada = ('2107', '2104', '2109')
list_bmw = ('M3', 'e34', 'x6')
list_mazda = ('6', 'cx5', '3')

avto = {'lada': list_lada, 'bmw': list_bmw, 'mazda': list_mazda }

print(list_lada[1], list_bmw[1], list_mazda[1])
print('lada -', avto['lada'], 'bmw -', avto['bmw'], 'mazda -', avto['mazda'])