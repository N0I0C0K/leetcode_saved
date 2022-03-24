from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        data = set()

        def dfs(node: TreeNode):
            if node is None:
                return
            nonlocal data
            data.add(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)

        def dfs2(node: TreeNode) -> bool:
            if node is None:
                return False
            nonlocal data, k
            if k-node.val in data and node.val + node.val != k:
                return True
            return dfs2(node.left) or dfs2(node.right)
        return dfs2(root)
