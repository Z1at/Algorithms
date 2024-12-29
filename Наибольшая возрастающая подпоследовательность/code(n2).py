from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    dp = [(1, nums[0])]
    n = len(nums)
    for i in range(1, n):
        mx = 0
        ind = -1
        for j in range(i):
            if dp[j][0] > mx and dp[j][1] < nums[i]:
                ind = j
                mx = dp[j][0]
        if ind != -1:
            dp.append((dp[ind][0] + 1, nums[i]))
        else:
            dp.append((1, nums[i]))
    return max([i[0] for i in dp])


