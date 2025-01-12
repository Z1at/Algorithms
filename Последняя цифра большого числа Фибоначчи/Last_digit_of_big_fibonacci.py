"""
https://stepik.org/lesson/13228/step/7?unit=3414

Необходимо найти последнюю цифру большого числа Фибоначчи

>>> last_digit(841645)
5
"""


def last_digit(n: int) -> int:
    f0, f1 = 0, 1
    for i in range(n - 1):
        f0, f1 = f1, (f0 + f1) % 10
    return f1
