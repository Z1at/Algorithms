"""
Given a number n, the task is to find the XOR from 1 to n.

>>> XOR(6)
7

>>> XOR(7)
0
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


"""
Объяснение алгоритма:
1- Find the remainder of n by moduling it with 4. 
2- If rem = 0, then XOR will be same as n. 
3- If rem = 1, then XOR will be 1. 
4- If rem = 2, then XOR will be n+1. 
5- If rem = 3 ,then XOR will be 0.
How does this work? 
When we do XOR of numbers, we get 0 as the XOR value just before a multiple of 4. 
This keeps repeating before every multiple of 4. 
"""