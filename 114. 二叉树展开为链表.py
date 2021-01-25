# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def flat(toor: TreeNode):
            if toor is None:
                return
            flat(toor.left)
            flat(toor.right)
            left: TreeNode = toor.left
            right: TreeNode = toor.right
            toor.left = None
            toor.right = left
            p = toor
            while(p.right is not None):
                p = p.right
            p.right = right
        flat(root)
        return root