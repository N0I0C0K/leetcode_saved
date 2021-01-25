class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def getRes(deep, toor: TreeNode) -> bool:
            if toor is None:
                return False
            if toor.right is None and toor.left is None:
                return deep+toor.val == sum 
            return getRes(deep+toor.val, toor.left) or getRes(deep+toor.val, toor.right)
        if not root:
            return False
        return getRes(0, root)