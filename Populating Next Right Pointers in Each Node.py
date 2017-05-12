__author__ = 'fafu'
class Solution:
    #Populating Next Right Pointers in Each Node
    def connect(self, root):
        if root is None:
            return None
        if root.left is None:
            return root
        node = root.left
        node.next = root.right
        parent = root
        stack = list()
        stack.append((root.right,root))
        while len(stack)>0:
            if node is None:
                node,parent = stack.pop()
            if parent.next is not None:
                node.next = parent.next.left
            while node.left is not None:
                node.left.next = node.right
                stack.append((node.right,node))
                parent = node
                node = node.left
            if node == parent.right and parent.next is not None:
                node.next = parent.next.left
            node = None
        return root
