# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр
# 6782 -> 23
# 0,56 -> 11

print('Введите число: ')
a = float(input())

def sum(x):
    result = 0
    while x != 0:
        result = result + x%10
        x = x/10
    return result

print(sum(a))
