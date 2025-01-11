"""
Finding first occurrence of an element.
bisect_left возвращает индекс самого левого вхождения элемента, если он есть, если его нет, то индекс первого числа,
больше заданного
"""

from bisect import bisect_left


def BinarySearch(a, x):
    i = bisect_left(a, x)
    print(i)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1


a = [1, 2, 4, 4, 8]
x = int(4)
res = BinarySearch(a, x)
if res == -1:
    print(x, "is absent")
else:
    print("First occurrence of", x, "is present at", res)


"""
Finding rightmost occurrence
bisect_right возвращает индекс самого правого вхождения элемента, если он есть, если его нет, то индекс первого числа,
больше заданного
"""
from bisect import bisect_right


def BinarySearch(a, x):
    i = bisect_right(a, x)
    print(i)
    if i != 0 and a[i - 1] == x:
        return i - 1
    else:
        return -1


a = [1, 2, 4, 4]
x = int(3)
res = BinarySearch(a, x)
if res == -1:
    print(x, "is absent")
else:
    print("Last occurrence of", x, "is present at", res)
