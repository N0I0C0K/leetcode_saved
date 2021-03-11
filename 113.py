#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        s_all = []
        def dfs(node:TreeNode, step:int, s:list):
            if node is None:
                s.append(0)
                return
            step += node.val
            s.append(node.val)
            if node.left is None and node.right is None:
                if step == targetSum:
                    s_all.append(s.copy())
            dfs(node.left, step, s)
            s.pop(-1)
            dfs(node.right, step, s)
            s.pop(-1)
        s = []
        dfs(root, 0, s)
        return s_all