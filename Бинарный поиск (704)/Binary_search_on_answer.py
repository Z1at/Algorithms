"""
https://stepik.org/lesson/311541/step/5?unit=293969

Задача про размещение дипломов на доске

>>> search(2, 3, 10)
9
"""


def check(ln, w, h):
    return (ln // w) * (ln // h)


def search(w: int, h: int, n: int) -> int:
    l = 0
    r = max(w, h) * n
    while l + 1 < r:
        mid = (l + r) // 2
        if check(mid, w, h) >= n:
            r = mid
        else:
            l = mid
    return r
