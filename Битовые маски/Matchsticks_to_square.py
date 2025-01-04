"""
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick.
You want to use all the matchsticks to make one square. You should not break any stick,
but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.

>>> makesquare([1,1,2,2,2])
True

>>> makesquare([3,3,4,4,4])
False
"""


from typing import List


def makesquare(matchsticks: List[int]) -> bool:

