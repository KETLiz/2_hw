# 3'. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# *Пример:*
# - Для n = 6: [2.0, 2.25, 2.37037037037037, 2.44140625, 2.4883199999999994, 2.5216263717421135]

n = int(input('Введите число: '))

sum = 0
for i in list(range(1, n+1)):
    res = float((1+1/i)**i)
    print(res, end = " ")
    sum += res
print()
print(f'Сумма чисел последовательности равна {sum}')
    