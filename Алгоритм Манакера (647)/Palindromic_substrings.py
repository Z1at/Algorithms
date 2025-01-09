"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

>>> countSubstrings("abc")
3

>>> countSubstrings("aaa")
6
"""


def countSubstrings(s: str) -> int:
    # Preprocess the string to insert '#' between characters and '^', '$' at the ends.
    # This helps to handle palindrome of even length properly.
    transformed_string = '^#' + '#'.join(s) + '#$'
    n = len(transformed_string)

    # Array to store the length of the palindrome centered at each character in T.
    palindrome_lengths = [0] * n

    # Current center, and the right boundary of the rightmost palindrome.
    center, right_boundary = 0, 0

    # Accumulator for the count of palindromic substrings.
    palindromic_substring_count = 0

    # Loop through the transformed string starting from the first character after '^'
    # and ending at the last character before '$'.
    for i in range(1, n - 1):
        # If the current position is within the rightmost palindrome, we can use
        # previously calculated data (palindrome_lengths[2 * center - i])
        # to determine the minimum length for the palindrome centered at i.
        if right_boundary > i:
            palindrome_lengths[i] = min(right_boundary - i, palindrome_lengths[2 * center - i])
        else:
            palindrome_lengths[i] = 1  # Start with a palindrome of length 1 (a single character).

        # Expand around the center i, and check for palindromes.
        while transformed_string[i + palindrome_lengths[i]] == transformed_string[i - palindrome_lengths[i]]:
            palindrome_lengths[i] += 1

        # Update the rightmost palindrome's boundary and center position
        # if the palindrome centered at i expands past it.
        if i + palindrome_lengths[i] > right_boundary:
            right_boundary = i + palindrome_lengths[i]
            center = i

        # Increment the count of palindromic substrings.
        # We divide by 2 because we inserted '#' and need the actual length.
        palindromic_substring_count += palindrome_lengths[i] // 2

    return palindromic_substring_count


"""
Весьма сложно кратко объяснить алгоритм, поэтому вот тут его можно найти https://algo.monster/liteproblems/647
"""