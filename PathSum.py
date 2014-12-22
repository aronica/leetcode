__author__ = 'fafu'
class Solution:
    #Path sum
    def hasPathSum(self, root, sum):
        if root.left is None and root.right is None:
            if sum == root.val:
                return True
            else:
                return False
        else:
            if root.left is not None:
                T = self.hasPathSum(self, root.left, sum - root.val)
                if T:
                    return True
            if root.right is not None:
                T = self.hasPathSum(self, root.left, sum - root.val)
                return T
