__author__ = 'fafu'
class Solution:
    def postorderTraversal(self, root):
        assert root is not None
        stack = list()
        result = list()
        node = root
        last = None
        while node is not None or len(stack) > 0:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if node.right is None or node.right == last:
                result.append(node.val)
                last = node
                node = None
            else:
                stack.append(node)
                node = node.right
        return result
