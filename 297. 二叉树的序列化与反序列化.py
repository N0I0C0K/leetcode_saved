#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root:TreeNode):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = []
        res = []
        queue.append(root)
        nums = 1
        res.append(root.val)
        while len(queue) > 0:
            for i in range(nums):
                temp:TreeNode = queue.pop(0)
                if temp:
                    queue.append(temp.left)
                    queue.append(temp.right)
            nums = len(queue)
            for i in range(nums):
                temp:TreeNode = queue[i]
                if temp:
                    res.append(temp.val)
                else:
                    res.append('null')
        return res
        

    def deserialize(self, data:list):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        root = TreeNode(0)
        nums = 1
        while len(data) > 0:
            for i in range(nums):
                temp = TreeNode(data.pop(0))
                if i%2 == 0:
                    root.left = temp
                else:
                    root.right = temp