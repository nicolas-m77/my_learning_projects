"""
 Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
 У пользователя необходимо запрашивать новый элемент рейтинга.
 Если в рейтинге существуют элементы с одинаковыми значениями,
 то новый элемент с тем же значением должен разместиться после них.
 Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
 Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
 Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
 Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
 Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""
# ПЕРВЫЙ ВАРИАНТ РЕШЕНИЯ, если НЕ ВАЖНО условие о том, что
# если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться ПОСЛЕ НИХ.

my_rating = [7, 5, 3, 3, 2]
print("Существующий рейтинг:", my_rating)
elem = int(input("Введите новый элемент рейтинга: "))
my_rating.append(elem)
print("Рейтинг после внесения нового элемента:", sorted(my_rating, reverse=True))
