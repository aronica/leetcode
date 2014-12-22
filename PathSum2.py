__author__ = 'fafu'
from Meta import TreeNode
class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        def __sums__(node,left,res,result):
            res.append(node.val)
            length = len(res)
            if node.left is None and node.right is None:
                if left == node.val:
                    result.append([i for i in res])
                return
            else:
                if node.left is not None:
                    __sums__(node.left,left - node.val,res,result)
                if node.right is not None:
                    res = res[0:length]
                    __sums__(node.right,left - node.val,res,result)

        if root is None:
            return []
        result = []
        res = []
        __sums__(root,sum,res,result)
        return result

