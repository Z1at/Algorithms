"""
Given an integer n, return the number of prime numbers that are strictly less than n.

>>> countPrime(10)
4
>>> countPrime(0)
0
>>> countPrime(1)
0
>>> countPrime(107)
27
"""


def countPrime(n: int) -> int:
    ans = []
    res = [True] * n
    for i in range(2, n):
        if res[i]:
            ans.append(i)
            for j in range(i + i, n, i):
                res[j] = False
    return len(ans)


"""
Создаём массив из True длиной n и начинаем перебирать все числа от 2 до n. Если res[i] = True, значит это простое число
Также, для каждого числа i мы перебираем все значения от i + i до n с шагом i и выставляем значения False, 
Это означает, что все эти числа делятся на i
Например: 
Мы берём 2 и ставим False на 4, 6, 8, 10 и тд. Потом берём 3 и ставим False на 6, 9, 12, 15 и тд
Потом пропускаем 4, так как там уже стоит False и это значит, что 4 делится на какое-то простое число
Берём 5, так как там ещё True и ставим False на 10, 15, 20, 25 и тд  
"""