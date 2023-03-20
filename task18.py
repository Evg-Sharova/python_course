"""Задача 18: Требуется найти в массиве A[1..N] самый близкий
 по величине элемент к заданному числу X. Пользователь в первой 
 строке вводит натуральное число N – количество элементов в массиве. 
 В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5"""
import random 

n = int(input("Введите кол-во элементов в массиве: "))
a = int(input("Введите искомое число: "))

from random import randint
mas = [randint(0, 10) for i in range(n)]
print(mas)

def nearest_num(mas, a):
    found = mas[0]        
    for x in mas:      
        if abs(x - a) < abs(found - a): 
            found = x 
    return found 
 
print(f'Ближайшее число к {a} в списке является {nearest_num(mas, a)}')