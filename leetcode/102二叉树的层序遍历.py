# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        quee = []
        quee.append(root)
        while len(quee) != 0:
            n = len(quee)
            quee_ = []
            for i in range(n):
                temp = quee.pop(0)
                quee_.append(temp.val)
                if temp.left != None:
                    quee.append(temp.left)
                if temp.right != None:
                    quee.append(temp.right)
            res.append(quee_)
        return res