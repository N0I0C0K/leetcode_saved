from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = l1
        b = l2
        c = ListNode(0, None)
        head = ListNode(0, c)
        e = 0
        while(a != None or b != None or e != 0):
            d = ListNode(0, None)
            if a!= None and b != None:
                d.val = (a.val+b.val+e)%10
                if a.val+b.val+e >= 10:
                    e = 1
                else:
                    e =0
                c.next = d
                c = d
                a = a.next
                b = b.next
            elif a != None:
                d.val = (a.val+e)%10
                if a.val+e >= 10:
                    e = 1
                else:
                    e =0
                c.next = d
                c = d
                a = a.next
            elif b != None:
                d.val = (b.val+e)%10
                if b.val+e >= 10:
                    e = 1
                else:
                    e =0
                c.next = d
                c = d
                b = b.next
            elif e == 1:
                d.val = 1
                c.next = d
                c = d
                e = 0
        return head.next.next