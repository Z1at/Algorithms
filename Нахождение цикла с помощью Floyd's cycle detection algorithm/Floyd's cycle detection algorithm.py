"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following
the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""

from typing import Optional

import pytest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: Optional[ListNode]) -> bool:
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False


def test_1():
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head

    assert hasCycle(head) is True


def test_2():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head

    assert hasCycle(head) is True


def test_3():
    head = ListNode(1)
    head.next = ListNode(3)

    assert hasCycle(head) is False


"""
Объяснение алгоритма:
При перемещении по списку медленный указатель будет перемещаться на один шаг за раз,
быстрый указатель перемещается на два шага за раз.
Если есть цикл, быстрый указатель в конечном итоге догонит медленный указатель в пределах цикла, 
потому что он движется быстрее.
Если цикла нет, быстрый указатель достигнет конца списка (т.е. станет нулевым).
Когда медленный и быстрый указатели встречаются, существует цикл или петля.
"""
