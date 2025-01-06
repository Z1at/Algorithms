import heapq

# В heapq мин-куча
# Чтобы получить макс-кучу, нужно добавлять числа с отрицательным знаком


hp = [4, 3, 2, 5, 1, 5, 1, 62, 5, 2, 5, 5, 3]
heapq.heapify(hp)  # принимает iterable и делает из этого кучу за линейное время in-place
print(hp)

heapq.heappush(hp, 0)
print(hp)

print(heapq.heappop(hp))
print(hp)


# heapq.nlargest(n, iterable, key=None)
# Return a list with the n largest elements from the dataset defined by iterable.

# heapq.nsmallest(n, iterable, key=None)
# Return a list with the n smallest elements from the dataset defined by iterable.


# Реализация heapsort
def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]


print(heapsort([4, 3, 2, 5, 1, 5, 1, 62, 5, 2, 5, 5, 3]))
