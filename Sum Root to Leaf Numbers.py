__author__ = 'fafu'
class Solution:
    def sumNumbers(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.val
        stack = list()
        node = root
        value = 0
        total = 0
        while len(stack)>0 or node is not None:
            if node is not None:
                if node.left is None and node.right is None:
                    total += value*10 + node.val
                    node = None
                else:
                    value = value*10 + node.val
                    stack.append((node,value))
                    node = node.left
            else:
                node,value = stack.pop()
                node = node.right
        return total
