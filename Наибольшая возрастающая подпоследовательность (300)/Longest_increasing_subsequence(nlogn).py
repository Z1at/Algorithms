"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.
algorithm that runs in O(n*(logn)) time complexity

>>> lengthOfLIS([10,9,2,5,3,7,101,18])
4
>>> lengthOfLIS([0,1,0,3,2,3])
4
>>> lengthOfLIS([7,7,7,7,7,7,7])
1
"""


from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    n = len(nums)
    d = [1e15] * (n + 1)
    pos = [0] * (n + 1)
    prev = [0] * (n + 1)
    length = 0

    pos[0] = -1
    d[0] = -1e15
    for i in range(n):
        l, r = 0, n
        while l < r:
            mid = l + (r - l) // 2
            if d[mid] < nums[i]:
                l = mid + 1
            else:
                r = mid
        if d[l - 1] < nums[i] < d[l]:
            d[l] = nums[i]
            pos[l] = i
            prev[i] = pos[l - 1]
            length = max(length, l)

    # Восстановление ответа
    answer = []
    p = pos[length]
    while p != -1:
        answer.append(nums[p])
        p = prev[p]
    answer.reverse()

    return len(answer)


"""
Используем следующий алгоритм: пусть d[i](i=0...n) — число, на которое оканчивается возрастающая последовательность 
длины i, а если таких чисел несколько — то наименьшее из них. 
Изначально мы предполагаем, что d[0]=−∞, а все остальные элементы d[i]= ∞. Заметим два важных свойства этой динамики: 
d[i−1]⩽d[i], для всех i=1...n и каждый элемент a[i] обновляет максимум один элемент d[j]. 
Это означает, что при обработке очередного a[i], мы можем за O(logn) c помощью двоичного поиска в массиве d 
найти первое число, которое больше либо равно текущего a[i] и обновить его.
Для восстановления ответа будем поддерживать заполнение двух массивов: pos и prev. 
В pos[i] будем хранить индекс элемента, на который заканчивается оптимальная подпоследовательность длины i, 
а в prev[i] — позицию предыдущего элемента для a[i].
"""