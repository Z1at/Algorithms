"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

>>> minSubArrayLen(7, [2,3,1,2,4,3])
2

>>> minSubArrayLen(4, [1,4,4])
1

>>> minSubArrayLen(11, [1,1,1,1,1,1,1,1])
0

>>> minSubArrayLen(11, [1,2,3,4,5])
3
"""


from typing import List
from collections import deque


def minSubArrayLen(target: int, nums: List[int]) -> int:
    """
    time - O(n), memory - O(n)
    """

    deq = deque()
    sm = 0
    ans = 1e15
    for i in nums:
        sm += i
        deq.append(i)
        while sm >= target:
            ans = min(ans, len(deq))
            sm -= deq.popleft()
    return ans if ans != 1e15 else 0


def minSubarrayLength(target: int, nums: List[int]) -> int:
    """
    time - O(n), memory - O(1)
    """
    # Initialize the length of the array
    length_of_nums = len(nums)
    # Set an initial answer value to a large number (beyond possible maximum)
    min_length = length_of_nums + 1
    # Initialize the sum of the current subarray and the start index j
    sum_of_subarray = start_index = 0
    # Loop over the elements in the array with their indices
    for end_index, value in enumerate(nums):
        # Add the current number to the sum of the current subarray
        sum_of_subarray += value
        # Shrink the subarray from the left (increase the start index)
        # until the sum is no longer greater or equal to the target
        while start_index < length_of_nums and sum_of_subarray >= target:
            # Update the minimum length if a shorter subarray is found
            min_length = min(min_length, end_index - start_index + 1)
            # Subtract the element at start_index from sum as we are excluding it from the subarray
            sum_of_subarray -= nums[start_index]
            start_index += 1
    # If min_length is updated, return it; otherwise, no such subarray exists and return 0
    return min_length if min_length <= length_of_nums else 0


"""
Объяснение алгоритма:
Добавляем элементы в дек пока их сумма не станет больше target, потом начинаем удалять элементы слева из дека,
при этом обновляя ответ
Функции отличаются только тем, что в первой используем дек, а во втором два указателя
"""
