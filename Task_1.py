# Задайте список из n чисел последовательности (1 + 1/n)^n.
# Вывести в консоль сам список и сумму его элементов.

# Вариант 1:
# number = int(input('Введите число: '))
# my_list = []
# for i in range(1, number + 1):
#     my_list.append(round((1 + 1 / i) ** i, 2))
# print(f'Список: {my_list}, \nСумма элементов списка равна {sum(my_list)}')

# Вариант 2:
number = int(input('Введите число: '))
def expression(x):
    return round((1 + 1 / x) ** x, 2)


my_list = [expression(i) for i in range(1, number + 1)]
print(f'Список: {my_list}\nСумма элементов списка равна {round(sum(my_list), 2)}')