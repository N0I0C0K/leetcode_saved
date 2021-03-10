#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(node: TreeNode,re: list):
            if node is None:
                return
            if node.left is None and node.right is None:
                re.append(node.val)
            dfs(node.left, re)
            dfs(node.right, re)
        r1 = []
        r2 = []
        dfs(root1, r1)
        dfs(root2, r2)
        if len(r1) == len(r2):
            for i in range(len(r1)):
                if r1[i] != r2[i]:
                    return False
            else:
                return True
        return False
