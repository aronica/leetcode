__author__ = 'fafu'
class Solution:
    #Same Tree Easy
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if (p is None and q is not None) or (p is not None and q is None):
            return False

        if p.val != q.val:
            return False

        T = self.isSameTree(p.left, q.left)
        if not T:
            return False
        T = self.isSameTree(p.right, q.right)
        return T
