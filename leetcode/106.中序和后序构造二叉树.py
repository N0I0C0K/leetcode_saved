# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(left_idx, right_idx):
            if left_idx > right_idx:
                return None
            val = postorder.pop(-1)
            root = TreeNode(val)
            idxx = idx_map[val]
            root.right = helper(idxx+1, right_idx)
            root.left = helper(left_idx, idxx-1)
            return root
        idx_map = {val:idx for idx, val in enumerate(inorder)}
        return helper(0, len(postorder)-1)