# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Было

# print("Введите число :")
# number = float(input())
# sum = 0
# for i in str(number):
#     if i != ".":
#         sum += int(i)

# print(f'Сумма чисел у введенного числа равна: {sum}.')


# Стало

my_num = int(input('Введите число: '))
print(sum(map(int,str(my_num))))