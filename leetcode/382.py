from typing import *
from random import *
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    head: ListNode = None
    thead: ListNode = None

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.thead = head
        pass

    def getRandom(self) -> int:
        n = randint(1, 10)
        for i in range(n):
            self.thead = self.thead.next
            if self.thead == None:
                self.thead = self.head
        return self.thead.val
