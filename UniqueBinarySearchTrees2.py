__author__ = 'fafu'
from Meta import TreeNode
class Solution:
    def generateTrees(self, n):
        if n == 1:
            return TreeNode(0)
        if n == 2:
            t1 = TreeNode(1)
            t1.right = TreeNode(2)
            t3 = TreeNode(2)
            t3.left = TreeNode(1)
            return [t1,t3]
        dp = ['#',[[1]],[[2,1],[1,'#',2]]]
        for i in xrange(3,n+1):
            res = []
            for j in xrange(0,n):
                result = [j]
                if j == 0:
                    result.append('#')
                    result.extend([m+1 for m in dp[i-1]])
                else:
                    pass





