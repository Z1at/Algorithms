"""
Given two integers left and right that represent the range [left, right],
return the bitwise AND of all numbers in this range, inclusive.

>>> rangeBitwiseAnd(5, 7)
4

>>> rangeBitwiseAnd(0, 0)
0

>>> rangeBitwiseAnd(1, 2147483647)
0

>>> rangeBitwiseAnd(67, 72)
64

>>> rangeBitwiseAnd(66, 66)
66
"""


def rangeBitwiseAnd(l: int, r: int) -> int:
    while l < r:
        r &= r - 1
    return r


"""
Объяснение алгоритма:
Простыми словами: мы каждый раз обнуляем самую правую единицу в r, так как если у нас в последовательности есть r - 1,
то r and (r - 1) обнулит самую правую единицу и она не попадёт в итоговый ответ.
То есть наш ответ - самая длинная подстрока из битов слева, которая есть у каждого числа из отрезка


The intuition behind the provided solution leverages the idea that the result of the bitwise AND operation of a range 
of numbers is determined by the common bits i.e., the bits that don't change across all numbers in the range. 
The moment a bit changes from 1 to 0 within the range, due to the nature of the AND operation 
(which requires all operands for a particular bit position to be 1 in order to yield a 1), 
that bit will be 0 in the final outcome.

The crucial observation is that if we progressively strip off the lowest bit of the 'right' number until it is less than
or equal to 'left', the bits that remain align with the bits of the final AND operation result.

Here's why:
If 'left' and 'right' are the same, the bits remain unchanged as there's nothing to compare or operate against, 
so the bitwise AND is equal to the 'left' or 'right' value.
If 'left' is less than 'right', at some point, the least significant bit that differs between 'left' and 'right' will 
become 0 in 'right' after a certain number of operations because 'right' will be decremented for every bit that is 1 
starting from the least significant bit.
Since 'right' is getting smaller with right & (right - 1) and 'left' is constant, eventually 'right' will be less than 
or equal to 'left' or the differing bits at the end of 'right' have been turned off.
The remaining bits before the changed bit in 'right' are common with 'left', therefore they remain unchanged and 
represent the bitwise AND of all numbers in the range.
"""