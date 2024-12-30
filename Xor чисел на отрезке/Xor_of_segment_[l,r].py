"""
Given two integers L and R, the task is to find the XOR of elements of the range [L, R].

>>> diff_XOR(4, 8)
8

>>> diff_XOR(3, 7)
3
"""


def XOR(n: int) -> int:
    if n % 4 == 0:
        return n

    if n % 4 == 1:
        return 1

    if n % 4 == 2:
        return n + 1

    if n % 4 == 3:
        return 0


def diff_XOR(l: int, r: int) -> int:
    xor_l = XOR(l - 1)
    xor_r = XOR(r)
    return xor_l ^ xor_r


"""
Объяснение алгоритма
We can find the XOR of elements from the range [1, N] in O(1) time. 
1) Find XOR of the range [1, L – 1]. Let this be x1.
2) Find XOR of the range [1, R].. Let this be x2.
3) Return XOR of x1 and x2

How does this work? We mainly get the elements from 1 to L-1 appeared twice in x1 ^ x2 and if we do XOR of an element 
with itself, we get 0 and if we do XOR of 0 with an element x, we get x.
"""