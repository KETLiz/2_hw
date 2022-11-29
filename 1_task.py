# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр
# 6782 -> 23
# 0,56 -> 11

print('Введите число: ')
a = float(input())

def Summa(x):
    result = 0
    for i in str(a):
        if i != '.':
            result = result + int(i)

    return result

print(f'Сумма цифр в числе равна: {Summa(a)}')