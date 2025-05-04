'''Задача 4. Самая популярная цифра'''

from statistics import mode

n = int(input('Введите число чисел:'))
print('Введите целое неотрицательное число:')

list_numbers = []

for _ in range(n):
    number = int(input())
    if number >= 0:
        list_numbers.append(number)

i = int(''.join(map(str, list_numbers)))

list_i = list(map(int, str(i)))

common_number = mode(list_i)

print('Часто встречающаяся цифра:')
print(common_number)


