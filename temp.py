#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next:ListNode = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = ListNode(0,head)
        res = cur
        while res.next and res.next.next:
            if res.next.val == res.next.next.val:
                x = res.next.next.val
                while res.next.next and res.next.next.val == x:
                    res.next.next = res.next.next.next
            else:
                res = res.next
        return cur.next