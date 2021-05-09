from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        temp = root
        self.display(res, root)
        return res

    def display(self, res: list, root: TreeNode):
        if root == None:
            return
        res.append(root.val)
        self.display(res, root.left)
        self.display(res, root.right)