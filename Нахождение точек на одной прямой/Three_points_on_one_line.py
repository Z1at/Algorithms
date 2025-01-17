"""
Вводится три точки в формате (x, y) вывести True, если эти точки лежат на одной прямой, False иначе

>>> check([(1, 1), (1, 4), (1, 5)])
True

>>> check([(1, 5), (2, 5), (4, 6)])
False
"""


from typing import List


def check(points: List[tuple[int, int]]) -> bool:
    x_1, y_1 = points[0]
    x_2, y_2 = points[1]
    x_3, y_3 = points[2]

    return (x_2 - x_1) * y_3 == (y_2 - y_1) * x_3 + y_1 * (x_2 - x_1) - x_1 * (y_2 - y_1)


"""
Для решение этой задачи, используем уравнение прямой y = kx + b. В него подставляем любые две точки и получаем, что
k = (y_2 - y_1) / (x_2 - x_1), b = y_1 - (x_1 * (y_2 - y_1)) / (x_2 - x_1)
Так как у нас есть формула прямой, то мы можем проверить лежит ли третья точка на этой прямой, если просто подставим
координаты третьй точки в формулу: y_3 = ((y_2 - y_1) / (x_2 - x_1)) * x_3 + y_1 - (x_1 * (y_2 - y_1)) / (x_2 - x_1)
Чтобы избежать деления на ноль, домножим на знаменатель и получим окончательную формулу:
(x_2 - x_1) * y_3 = (y_2 - y_1) * x_3 + y_1 * (x_2 - x_1) - x_1 * (y_2 - y_1)
"""