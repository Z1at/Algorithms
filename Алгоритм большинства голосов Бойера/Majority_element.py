"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

>>> majorityElement([3,2,3])
3

>>> majorityElement([2,2,1,1,1,2,2])
2
"""


from typing import List


def majorityElement(nums: List[int]) -> int:
    count, ans = 1, nums[0]
    for i in nums[1:]:
        if i == ans:
            count += 1
        elif count == 0:
            ans = i
            count = 1
        else:
            count -= 1
    return ans


"""
Объяснение алгоритма:
The solution uses the Moore Voting Algorithm, which is efficient in finding the majority element of an array when such 
an element definitely exists.

The algorithm works in a single pass and uses constant extra space. It consists of two main variables: the candidate m 
representing the presumed majority element, and the counter cnt indicating the strength of our presumption that m is 
indeed the majority element.

To implement the algorithm, we iterate through each element x of the array nums. During this iteration, the following 
logic is applied:

When cnt equals zero, there's no current candidate for majority element, or the previous candidate has been completely 
offset by other elements. So we assign the current element x to be the new candidate m, and set cnt to 1, 
because we start counting the occurrences of m again.
If cnt is not zero, it means there's a candidate set and we need to compare the current element x with m.
If x is equal to m, this means we've found another instance of our candidate, and we increment the counter cnt by 1, 
strengthening the candidacy of m.
If x is not equal to m, this means we have encountered an element that opposes our candidate. To denote this opposition, 
we decrement the counter cnt by 1.
By the end of the loop, despite all the increments and decrements, the surplus repetitions of the majority element 
ensure that m will remain as the candidate and cnt will be greater than zero.

Given the guarantee that a majority element always exists, m is the majority element at the end of this single pass, 
and we can return m as the answer.

It's important to note that if the problem statement didn't guarantee the existence of a majority element, a second pass
would be necessary to confirm that our candidate m is indeed the majority by counting its total occurrences in nums and
comparing it to n / 2.
"""