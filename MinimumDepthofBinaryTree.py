__author__ = 'fafu'
class Solution:
    def minDepth(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        elif root.left is not None and root.right is not None:
            left = self.minDepth(root.left)
            right = self.minDepth(root.right)
            return min(left, right) + 1
        elif root.left is not None:
            return self.minDepth(root.left) + 1
        else:
            return self.minDepth(root.right) + 1
