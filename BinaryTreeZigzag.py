__author__ = 'fafu'
from Meta import TreeNode
class Solution:
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [[root.val]]
        result = []
        stack = [root]
        order = True
        while len(stack)>0:
            if order:
                result.append([node.val for node in stack])
                order = False
            else:
                result.append([node.val for node in stack])
                result[-1].reverse()
                order = True
            stack2 = []
            for i in stack:
                if i.left is not None:
                    stack2.append(i.left)
                if i.right is not None:
                    stack2.append(i.right)
            stack = stack2
        return result
n1 = TreeNode(1)

n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n8 = TreeNode(8)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7

n4.right = n8


s = Solution()
n = s.zigzagLevelOrder(n1)
print n






