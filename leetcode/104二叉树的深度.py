class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def getDeep(deep: int, root: TreeNode) ->int:
            deep += 1
            if not root:
                return deep
            return max(getDeep(deep, root.left), getDeep(deep, root.right))
        return getDeep(1, root)