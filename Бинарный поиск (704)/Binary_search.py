"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search
target in nums. If target exists, then return its index. Otherwise, return -1.

>>> search([-1,0,3,5,9,12], 9)
4

>>> search([-1,0,3,5,9,12], 2)
-1
"""


from typing import List


def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] >= target:
            r = mid
        else:
            l = mid + 1

    return l if nums[l] == target else -1
