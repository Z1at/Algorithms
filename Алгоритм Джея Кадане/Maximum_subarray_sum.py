"""
Given an array arr[], the task is to find the subarray that has the maximum sum and return its sum.

>>> maxSubarraySum([2,3,-8,7,-1,2,3])
11

>>> maxSubarraySum([-2,-4])
-2

>>> maxSubarraySum([5,4,1,7,8])
25
"""


from typing import List


def maxSubarraySum(nums: List[int]) -> int:
    res = nums[0]
    maxEnding = nums[0]

    for i in range(1, len(nums)):
        # Find the maximum sum ending at index i by either extending
        # the maximum sum subarray ending at index i - 1 or by
        # starting a new subarray from index i
        maxEnding = max(maxEnding + nums[i], nums[i])

        # Update res if maximum subarray sum ending at index i > res
        res = max(res, maxEnding)

    return res


"""
The idea of Kadane’s algorithm is to traverse over the array from left to right and for each element, find the maximum 
sum among all subarrays ending at that element. The result will be the maximum of all these values. 


But, the main issue is how to calculate maximum sum among all the subarrays ending at an element in O(1) time?


To calculate the maximum sum of subarray ending at current element, say maxEnding, we can use the maximum sum ending at 
the previous element. So for any element, we have two choices:


Choice 1: Extend the maximum sum subarray ending at the previous element by adding the current element to it. If the 
maximum subarray sum ending at the previous index is positive, then it is always better to extend the subarray.
Choice 2: Start a new subarray starting from the current element. If the maximum subarray sum ending at the previous 
index is negative, it is always better to start a new subarray from the current element.
This means that maxEnding at index i = max(maxEnding at index (i – 1) + arr[i], arr[i]) and the maximum value of 
maxEnding at any index will be our answer. 
"""