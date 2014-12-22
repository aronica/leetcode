__author__ = 'fafu'
class Solution:
    def inorderTraversal(self, root):
        if root is None or len(root)==0:
            return []
        res = []
        stack = []
        node = root
        while node is not None or len(stack)>0:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                res.append(node.val)
                if node.right is not None:
                    node = node.right
                else:
                    node = None
        return res
