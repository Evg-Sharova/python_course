"""Задача 30:  Заполните массив элементами 
арифметической прогрессии. Её первый элемент, 
разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки."""

a1 = int(input("Введите первое число массива: "))
d = int(input("Введите значение разности: "))
n = int(input("Введите кол-во элементов массива: "))

result = [a1]
for a in range(1, n):
    a = a1 + (n-1) * d  
    result.append(a)
    a1 = a
    
print(result) 