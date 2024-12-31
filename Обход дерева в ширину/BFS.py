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

4 1 2 5 3

4 6
3 4
2 4
1 3
1 2
1 4
2 3
4

4 3 2 1
"""


from queue import Queue
from collections import defaultdict


n, m = map(int, input().split())
used = [False] * (n + 1)
ans = []
q = Queue()
links = defaultdict(list)


def bfs() -> None:
    if q.empty():
        return
    while q.qsize():
        v = q.get()
        ans.append(v)
        for u in links[v]:
            if used[u]:
                continue
            used[u] = True
            q.put(u)


def solution(n: int, m: int) -> None:
    for i in range(m):
        v, u = map(int, input().split())
        links[v].append(u)
        links[u].append(v)

    v = int(input())
    q.put(v)
    used[v] = True
    bfs()


solution(n, m)
print(*ans)


"""
Объяснение алгоритма:
Аналогично bfs используем массив, чтобы хранить какие вершины мы уже посетили. Используем словарь для составления рёбер.
Используем очередь, чтобы хранить в каком порядке будем перебирать вершины. Каждый раз в очередь добавляем все рёбра,
которые приведут к ещё не посещённым узлам
"""