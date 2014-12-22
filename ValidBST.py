__author__ = 'fafu'
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        def __isBST__(node,mins,maxes):
            if node is None:
                return True
            if mins is not None and maxes is not None:
                if node.val>mins and node.val<maxes:
                    return __isBST__(node.left,mins,node.val) and __isBST__(node.right,node.val,maxes)
            elif mins is not None and maxes is None:
                if node.val>mins:
                    return __isBST__(node.left,mins,node.val) and __isBST__(node.right,node.val,maxes)
            elif maxes is not None and mins is None:
                if node.val<maxes:
                    return __isBST__(node.left,mins,node.val) and __isBST__(node.right,node.val,maxes)
            elif mins is None and maxes is None:
                return __isBST__(node.left,mins,node.val) and __isBST__(node.right,node.val,maxes)
            return False
        return __isBST__(root,None,None)






