"""
https://stepik.org/lesson/307318/step/6?unit=289406

В отсортированном массиве первое число, которое больше либо равно числу из запроса
"""


from typing import List


def search(nums: List[int], target: int) -> int:
    if target > nums[-1]:
        return int(1e15)

    l, r = -1, len(nums)
    while l + 1 < r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid
        else:
            r = mid

    return nums[r]
