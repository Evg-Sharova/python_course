"""Задача 16: Требуется вычислить, сколько раз встречается некоторое 
число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное 
число N – количество элементов в массиве. В последующих  строках записаны N 
целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    3
    -> 1"""
import random 

n = int(input("Введите кол-во элементов в массиве: "))
a = int(input("Введите искомое число: "))

from random import randint
mas = [randint(0, 10) for i in range(n)]
print(mas)
result = []
for x in mas:
    if x == a:
        result.append(x)
    
print(result)
print(len(result))

