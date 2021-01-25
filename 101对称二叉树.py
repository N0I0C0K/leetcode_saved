#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        a = []
        b = []
        self.display(a, root)
        self.display_(b, root)
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        return True
        

    def display_(self, res: list, root: TreeNode):
        if root == None:
            res.append(-1)
            return
        res.append(root.val)
        if not root.left and not root.right:
            return
        self.display_(res, root.left)
        self.display_(res, root.right)

    def display(self, res: list, root: TreeNode):
        if root == None:
            res.append(-1)
            return
        res.append(root.val)
        if not root.left and not root.right:
            return
        self.display(res, root.right)
        self.display(res, root.left)