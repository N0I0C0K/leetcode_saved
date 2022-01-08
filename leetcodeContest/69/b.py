# Definition for singly-linked list.
from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = 0
        thead = head
        while thead != None:
            n += 1
            thead = thead.next
        t = 0
        to = []
        maxr = 0
        thead = head
        while thead != None:
            t += 1
            if t <= (n >> 1):
                to.append(thead.val)
            else:
                if thead.val+to[n-t] > maxr:
                    maxr = thead.val+to[n-t]
            thead = thead.next
        return maxr
