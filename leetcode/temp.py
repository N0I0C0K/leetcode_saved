from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans: str = ''

        def dfs(node: TreeNode):
            if node is None:
                return
            nonlocal ans
            ans += str(node.val)
            if node.left is None and node.right is None:
                return
            if node.right is not None:
                ans += '('
                dfs(node.left)
                ans += ')('
                dfs(node.right)
                ans += ')'
            else:
                ans += '('
                dfs(node.left)
                ans += ')'
        dfs(root)
        return ans
