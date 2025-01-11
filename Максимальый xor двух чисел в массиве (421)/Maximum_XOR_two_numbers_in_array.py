"""
Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.

>>> findMaximumXOR([3,10,5,25,2,8])
28

>>> findMaximumXOR([14,70,53,83,49,91,36,80,92,51,66,70])
127
"""


from typing import List


def findMaximumXOR(nums: List[int]) -> int:
    maximum_xor = 0  # Initialize the maximum XOR value.
    mask = 0  # Initialize the mask, which is used to consider bits from the most significant bit down.

    # Start from the highest bit and go down to the least significant bit (31st to 0th bit).
    for i in range(31, -1, -1):
        mask = mask | (1 << i)  # Update the mask to include the next bit.
        prefixes = set()  # Create a set to store prefixes of the current length.

        # Collect all prefixes with bits up to the current bit.
        for num in nums:
            prefixes.add(num & mask)  # Bitwise AND to isolate the prefix.

        # We assume the new bit is '1' and combine it with maximum XOR so far.
        proposed_max = maximum_xor | (1 << i)

        # Check if there's a pair of prefixes which XOR equals our proposed maximum so far.
        for prefix in prefixes:
            if (prefix ^ proposed_max) in prefixes:
                maximum_xor = proposed_max  # Update the maximum XOR since we found a pair.
                break  # No need to check other prefixes.

    # After checking all bits, return the maximum XOR we found.
    return maximum_xor


"""
https://algo.monster/liteproblems/421
"""