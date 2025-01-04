"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""


from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    def depth_first_search(index: int):
        # Once we've considered all elements, take a snapshot of the current subset
        if index == len(nums):
            all_subsets.append(current_subset[:])
            return

        # Exclude the current element and move to the next
        depth_first_search(index + 1)

        # Include the current element and move to the next
        current_subset.append(nums[index])
        depth_first_search(index + 1)

        # Backtrack: remove the current element before going up the recursion tree
        current_subset.pop()

    # This list will hold all the subsets
    all_subsets = []
    # This is a temporary list to hold the current subset
    current_subset = []
    # Start the depth-first search from index 0
    depth_first_search(0)
    # Return the final list of all subsets
    return all_subsets
