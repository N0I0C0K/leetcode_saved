# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def invTree(toor: TreeNode):
            if toor is None:
                return
            temp = toor.left
            toor.left = toor.right
            toor.right = temp
            invTree(toor.left)
            invTree(toor.right)
            return
        invTree(root)
        return root