"""
5 7
3 5
1 4
1 2
2 4
4 5
3 4
1 3
4

9
4 1 2 1 3 5 3 1 4

4 6
3 4
2 4
1 3
1 2
1 4
2 3
4

7
4 3 1 2 1 3 4
"""


from collections import defaultdict


n, m = map(int, input().split())
used = [False] * (n + 1)
ans = []
voc = defaultdict(list)


def dfs(v: int) -> None:
    ans.append(v)
    used[v] = True
    for u in voc[v]:
        if used[u]:
            continue
        dfs(u)
        ans.append(v)


def solution(n: int, m: int) -> None:
    for i in range(m):
        x, y = map(int, input().split())
        voc[x].append(y)
        voc[y].append(x)
    v = int(input())
    dfs(v)


solution(n, m)
print(len(ans))
print(*ans)


"""
Объяснение алгоритма:
Мы сначала читаем все данные, создаём словарь с всеми связями, после этого запускаем dfs.
dfs работает так, что в начале мы добавляем нашу вершину в ответ, помечаем, что уже были в ней
Потом перебираем все рёбра и ходим во все, который ещё не были посещены
"""