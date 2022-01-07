class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return abs(self.getDeep(root.left) - self.getDeep(root.right)) <= 1 and self.isBalanced(root.right) and self.isBalanced(root.left)

    def getDeep(self, root: TreeNode) -> int:
        if root == None:
            return 0
        return 1+max(self.getDeep(root.left), self.getDeep(root.right))
