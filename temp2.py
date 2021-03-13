#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(node: TreeNode):
            if node == None:
                return 0
            he_le = dfs(node.left)
            he_ri = dfs(node.right)
            if abs(he_le - he_ri) > 1:
                return -10
            if he_le == -10 or he_ri == -10:
                return -10
            he = max(he_le, he_ri)
            return he+1
        
        return True if dfs(root) != -10 else False
            
