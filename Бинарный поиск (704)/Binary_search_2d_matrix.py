"""
You are given an m x n integer matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

Example:
    [[1,3,5,7],
    [10,11,16,20],
    [23,30,34,60]]

>>> searchMatrix([[1,3,5,7], [10,11,16,20], [23,30,34,60]], 3)
True

>>> searchMatrix([[1,3,5,7], [10,11,16,20], [23,30,34,60]], 13)
False
"""


from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    # Get the number of rows and columns in the matrix
    num_rows, num_columns = len(matrix), len(matrix[0])

    # Initialize pointers for the binary search
    left, right = 0, num_rows * num_columns - 1

    # Conduct a binary search in the matrix
    while left < right:
        # Calculate the middle index between left and right
        mid = (left + right) >> 1  # Equivalent to floor division by 2 (mid = (left + right) // 2)
        # Convert the 1D representation mid back to 2D indices x and y
        row, column = divmod(mid, num_columns)
        # If the middle element is greater or equal to the target, go left
        if matrix[row][column] >= target:
            right = mid
        # If the middle element is less than the target, go right
        else:
            left = mid + 1

    # After the loop, left should point to the target element if it exists
    # Check if the target is indeed at the (left // num_columns, left % num_columns) position
    return matrix[left // num_columns][left % num_columns] == target


"""
Данное решение заключается в том, что мы работает с двумерным массивом как с одномерным 


Самое простое решение - перевести двумерный массив в одномерный с помощью extend и в нём провести бинарный поиск, 
но тогда мы будем использовать дополнительную память, что нежелательно:
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    lst = []
    for i in matrix:
        lst.extend(i)

    l, r = 0, len(lst) - 1
    while l < r:
        mid = (l + r) // 2
        if lst[mid] >= target:
            r = mid
        else:
            l = mid + 1
    return lst[l] == target


Второе решение заключается в использовании двух раз бинарный поиск:
Сначала мы запускаем бинарный поиск по первому стобцу и находим такую строку i,
что matrix[i][0] <= target и matrix[i + 1][0] > target, это будет означать, что target может лежать в строке i
Дальше мы запускаем бинарный поиск в matrix[i] и проверяем есть ли там target
Данное решение не работает при matrix = [[1,3]] и target = 3
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    if target < matrix[0][0] or target > matrix[-1][0]:
        return False

    l, r = 0, len(matrix) - 1
    while l + 1 < r:
        mid = (l + r) // 2
        if matrix[mid][0] >= target:
            r = mid
        else:
            l = mid

    line = l

    l, r = 0, len(matrix[0]) - 1
    while l < r:
        mid = (l + r) // 2
        if matrix[line][mid] >= target:
            r = mid
        else:
            l = mid + 1

    return matrix[line][l] == target
"""