""" Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать
в виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной
функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень
с помощью оператора **. Второй — более сложная реализация без оператора **,
предусматривающая использование цикла."""


def my_func(a, b):
    n = 1
    for i in range(abs(b)):
        n = n * (1 / a)
    return n


x = float(input("Введите действительное положительное число x: "))
y = int(input("Введите целое отрицательное число y: "))
print("x в степени y равно", my_func(x, y))
