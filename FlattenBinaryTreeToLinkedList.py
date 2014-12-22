__author__ = 'fafu'
from Meta import TreeNode
class Solution:
    def flatten(self, root):
        if root is None or root.left is None and root.right is None:
            return root
        stack = list()
        node = root
        last = None
        while node is not None or len(stack)>0:
            if node is not None:
                if node.right is not None:
                    stack.append(node.right)
                if node.left is not None:
                    node.right = node.left
                else:
                    pass
                last = node
                node = node.left
                last.left = None
            else:
                node = stack.pop()
                if last is not None:
                    last.right = node
        return root

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
n = s.flatten(n1)
print n
