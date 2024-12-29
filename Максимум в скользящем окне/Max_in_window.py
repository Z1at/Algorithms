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


print(*maxSlidingWindow([2, 3, 9], 3))
