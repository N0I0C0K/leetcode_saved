# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        quee = []
        quee.append(root)
        while len(quee) != 0:
            num = len(quee)
            right: Node = None
            for i in range(num):
                toor = quee.pop(0)
                if toor.left is not None:
                    if right is not None:
                        right.next = toor.left
                    toor.left.next = toor.right
                    right = toor.right
                    quee.append(toor.left)
                    quee.append(toor.right)
        return root
