"""
https://stepik.org/lesson/307327/step/6?unit=289415

Задача про количество способов добраться роботу из левого верхнего угла в правый нижний
"""


from typing import List


def robot(n: int, m: int, matrix: List[List[int]]) -> int:
    dp = [[0] * (m + 1) for i in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0 and (dp[i][j + 1] != 0 or dp[i + 1][j] != 0 or dp[i][j] != 0):
                dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j] + dp[i][j]

    return dp[-1][-1] % 1000000009


n, m = map(int, input().split())
print(robot(n, m, [[int(j) for j in input().split()] for i in range(n)]))


"""
Просто создаём внешнюю оболочку для удобства и потом проходим по двумерному массиву и считаем количество способов
попасть в i клетку, как сумма [i - 1][j], [i][j - 1], [i - 1][j - 1]
"""