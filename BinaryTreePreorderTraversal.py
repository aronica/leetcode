__author__ = 'fafu'
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        assert root is not None
        stack = list()
        result = list()

        node = root
        stack.append(node)

        while len(stack) > 0:
            node = stack.pop()
            result.append(node.val)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return result
