"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def dividing(c, d):
    return c / d


a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
if b == 0:
    print("Делить на ноль нельзя!")
else:
    print("Результат деления a на b:", dividing(a, b))