# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(left_idx, right_idx):
            if left_idx > right_idx:
                return None
            val = preorder.pop(0)
            root = TreeNode(val)
            idxx = idx_map[val]
            root.left = helper(left_idx, idxx-1)
            root.right = helper(idxx+1, right_idx)
            return root
        idx_map = {val:idx for idx, val in enumerate(inorder)}
        return helper(0, len(preorder)-1)