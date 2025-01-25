"""
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and
then concatenate all the integers.

Return the number of different expressions that you can build, which evaluates to target.


"""


from typing import List


def findTargetSumWays(self, nums: List[int], target: int) -> int:
    # Calculate the sum of all numbers in the array
    total_sum = sum(nums)

    # Check if the target is achievable or not
    # If the sum of nums is less than target, or the difference between sum and target
    # is not an even number, then return 0 because target can't be achieved
    if total_sum < target or (total_sum - target) % 2 != 0:
        return 0

    # Compute the subset sum we need to find to partition the array
    # into two subsets that give the desired target on applying + and - operations
    subset_sum = (total_sum - target) // 2

    # Initialize a list for dynamic programming, with a size of subset_sum + 1
    dp = [0] * (subset_sum + 1)

    # There is always 1 way to achieve a sum of 0, which is by selecting no elements
    dp[0] = 1

    # Update the dynamic programming table
    # For each number in nums, update the count of ways to achieve each sum <= subset_sum
    for num in nums:
        for j in range(subset_sum, num - 1, -1):
            # Add the number of ways to achieve a sum of j before num was considered
            dp[j] += dp[j - num]

    # Return the number of ways to achieve subset_sum, which indirectly gives us the number of ways
    # to achieve the target sum using '+' and '-' operations
    return dp[-1]

