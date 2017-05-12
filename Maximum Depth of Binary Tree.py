__author__ = 'fafu'
class Solution:
    #Maximum Depth of Binary Tree
    def maxDepth(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        left = 0
        right = 0
        if root.left is not None:
            left = self.maxDepth(root.left)
        if root.right is not None:
            right = self.maxDepth(root.right)
        return max(left+1,right+1)
