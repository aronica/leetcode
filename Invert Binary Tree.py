__author__ = 'fafu'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None or root.left is None and root.right is None:
            return root

        if root.left is None and root.right is not None:
            root.left = root.right
            root.right = None
            self.invertTree(root.left)
        elif root.right is None and root.left is not None:
            root.right = root.left
            root.left = None
            self.invertTree(root.right)
        else:
            oldleft = root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(oldleft)
        return root