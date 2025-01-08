"""
https://stepik.org/lesson/307318/step/9?unit=289406

В отсортированном массиве последнее число, которое меньше числа из запроса
"""


from typing import List


def search(nums: List[int], target: int) -> int:
    if target <= nums[0]:
        return -int(1e15)
    target -= 1

    l, r = -1, len(nums)
    while l + 1 < r:
        mid = (l + r) // 2
        if nums[mid] > target:
            r = mid
        else:
            l = mid

    return nums[r]
