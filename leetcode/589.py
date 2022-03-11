from typing import *
# Definition for a Node.


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans: List[int] = []

        def dfs(root: 'Node'):
            if root == None:
                return
            nonlocal ans
            ans.append(root.val)
            for child in root.children:
                dfs(child)
        dfs(root)
        return ans
