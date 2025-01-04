"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.
algorithm that runs in O(n ** 2) time complexity

>>> lengthOfLIS([10,9,2,5,3,7,101,18])
4
>>> lengthOfLIS([0,1,0,3,2,3])
4
>>> lengthOfLIS([7,7,7,7,7,7,7])
1
"""


from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    dp = [(1, nums[0])]
    n = len(nums)
    for i in range(1, n):
        mx = 0
        for j in range(i):
            if dp[j][0] > mx and dp[j][1] < nums[i]:
                mx = dp[j][0]
        dp.append((mx + 1, nums[i]))
    return max([i[0] for i in dp])


"""
Объяснение алгоритма:
Используем динамическое программирование, состояние динамики - самая длинная подпоследовательность на момент i.
База - (1 = длина самой длинной подпоследовательности, nums[0] - первый элемент). 
Перебираем все числа последовательности и для каждого из них перебираем все элементы dp до нашего.
Если dp[j][0] > mx, то есть длина у элемента j больше, чем наша на данный момент и наше число больше рассматриваемого,
то мы обновляем mx. 
Потом в dp кладём максимально найденную длину + 1 и наш элемент
"""
