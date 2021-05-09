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
            all = 0
            for i in range(num):
                toor = quee.pop(0)
                if toor.left is not None:
                    quee.append(toor.left)
                    all += 1
                if all >= 2:
                    quee[-2].next = quee[-1]
                if toor.right is not None:
                    quee.append(toor.right)
                    all += 1
                if all >= 2:
                    quee[-2].next = quee[-1]
        return root