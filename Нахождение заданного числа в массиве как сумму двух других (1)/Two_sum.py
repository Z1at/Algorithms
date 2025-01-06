"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

>>> twoSum([2,7,11,15], 9)
[0, 1]

>>> twoSum([3,2,4], 6)
[1, 2]

>>> twoSum([3,3], 6)
[0, 1]
"""


from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    # Create a dictionary to store numbers and their indices
    index_map = {}
    # Enumerate through the list of numbers
    for index, number in enumerate(nums):
        # Calculate the complement of the current number
        complement = target - number
        # If complement is in the index_map, a solution is found
        if complement in index_map:
            # Return the indices of the two numbers
            return [index_map[complement], index]
        # Otherwise, add the current number and its index to the index_map
        index_map[number] = index
    # If no solution is found, this return will not be reached due to guaranteed solution.


"""
Есть и другое решение через сортирование массива с запоминанием индексов и потом через два указателя найти ответ
"""