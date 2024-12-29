"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left
of the array to the very right. You can only see the k numbers in the window.
Each time the sliding window moves right by one position.
Return the max sliding window.

>>> maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
[3, 3, 5, 5, 6, 7]
>>> maxSlidingWindow([2, 3, 9], 2)
[3, 9]
>>> maxSlidingWindow([1], 1)
[1]
"""


from typing import List


def maxSlidingWindow(nums: List[int], k: int) -> list[float]:
    stack1 = [[-1e10, -1e10]]
    stack2 = [[-1e10, -1e10]]
    ans = []
    for i in nums:
        if len(stack1) == 1:
            stack1.append([i, i])
        else:
            stack1.append([i, max(stack1[-1][1], i)])
        if len(stack1) == k + 1:
            while len(stack1) > 1:
                stack2.append([stack1[-1][0], max(stack1[-1][0], stack2[-1][1])])
                stack1.pop()
        if len(stack1) + len(stack2) == k + 2:
            ans.append(max(stack1[-1][1], stack2[-1][1]))
            if len(stack2) > 1:
                stack2.pop()
    return ans


"""
Объяснение алгоритма:
Используем два стека, добавляем в первый стек значения (значение из массива, максимальное значение стека на данный момент)
Как только первый стек будет длиной k + 1 (потому что нулевой элемент мы добавили заранее),
Мы достаём из него поочереди элементы и аналогичным образом добавляем (значение на данный момент, максимальное значение)
во второй стек, пока в первом не останется один элемент.
Когда у нас сумма длин первого и второго стека становится равна k + 2 (мы наполнили окно), 
то мы выбираем максимум среди значений стеков, добавляем в ответ и удаляем значение из второго стека, 
если его длина больше 1

Для реализации минимума в окне, нужно заменить все функции max на min
"""