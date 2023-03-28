"""Задача 32: Определить индексы элементов массива 
(списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)"""

import random 

n = int(input("Введите кол-во элементов в массиве: "))
min = int(input("Введите минимальное значение диапазона: "))
max= int(input("Введите максимальное значение диапазона: "))

from random import randint

mas = [randint(0, 10) for i in range(n)]
print(mas)

print(list(map(lambda x: min < x < max, mas)))

result = []
for i in range(0, len(mas)):
    if min < mas[i] < max:
        result.append(i)
print(result)