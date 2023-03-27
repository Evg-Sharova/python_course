"""Задача 22: Даны два неупорядоченных набора целых чисел 
(может быть, с повторениями). Выдать без повторений в порядке 
возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств."""

import random 

n = int(input("Введите кол-во элементов в массиве 1: "))
m = int(input("Введите кол-во элементов в массиве 2: "))

from random import randint
mas1 = [randint(0, 10) for i in range(n)]
mas2 = [randint(0, 10) for i in range(m)]
print(mas1)
print(mas2)

result = []
count = 0
for i in range(len(mas1)):
    for j in range(len(mas2)):
        if mas1[i] == mas2[j]:
            result.append(mas1[i])
            count += 1
print(count)
print(result)
res = sorted(result)
print(res)
      

               


