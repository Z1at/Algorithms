"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

>>> generateParenthesis(3)
["((()))","(()())","(())()","()(())","()()()"]

>>> generateParenthesis(1)
["()"]
"""

from typing import List


def generateParenthesis(n: int) -> List[str]:
    # Helper function for depth-first search
    def backtrack(open_count, close_count, path):
        # If there are more open or more close parens than 'n', or more close parens than open, it's invalid
        if open_count > n or close_count > n or open_count < close_count:
            return
        # When the current path uses all parens correctly, add the combination to the results
        if open_count == n and close_count == n:
            combinations.append(path)
            return
        # Continue the search by adding an open paren if possible
        backtrack(open_count + 1, close_count, path + '(')
        # Continue the search by adding a close paren if possible
        backtrack(open_count, close_count + 1, path + ')')

    # This list will hold all the valid combinations
    combinations = []
    # Start the recursive search with initial counts of open and close parentheses
    backtrack(0, 0, '')
    # Return all the valid combinations found
    return combinations
