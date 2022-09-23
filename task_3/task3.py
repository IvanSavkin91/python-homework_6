# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Было

# n = [i for i in range(1, 10)]
# print(n)
# print(f'Ответ: {sum([n[i] for i in range(1, len(n), 2)])}')


# Стало

from random import randint
n = int(input('Введите размер списка: '))
a = []
for i in range(n):
    a.append(randint(1, 10))
print(f'Первоначальный список {a}')
new_numb = list(filter(lambda x: (x % 2 == 1) , a))
print('Сумма четных чисел равна : '+ str(sum(new_numb)))