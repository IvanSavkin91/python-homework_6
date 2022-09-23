# Реализуйте алгоритм перемешивания списка.
# Было

# from random import randint
 
# n = int(input('Введите размер списка: '))
# a = []
# for i in range(n):
#     a.append(randint(1, 150))
# print(f'Первоначальный список {a}')
 
 
# for i in range(n-1):
#     for j in range(n-i-1):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
 
# print(f'Отсортированный список методом пузырька {a}')

# Стало

import random
my_list = [random.randint(1,10) for i in range(random.randint(3,8))]
print(f"Наш список: {my_list}")
random.shuffle(my_list)
print(f"Наш список после перемешивания: {my_list}")
