from Meta import TreeNode
import Meta
class Solution:
    def connect(self, root):
        if root is None or root.left is None and root.right is None:
            return root
        stack = list([root])
        root.next = None
        while len(stack) > 0:
            node = stack.pop(0)
            tmp = node.left or node.right
            while tmp is not None:
                if node.left is not None and tmp is node.left and node.right is not None:
                    node.left.next = node.right
                else:
                    next = node.next
                    found = False
                    while next is not None:
                        if next.left is not None:
                            tmp.next = next.left
                            found = True
                            break
                        elif next.right is not None:
                            tmp.next = next.right
                            found = True
                            break
                        else:
                            next = next.next
                    if not found:
                        tmp.next = None
                stack.append(tmp)
                if tmp is node.left:
                    tmp = node.right
                else: break



s = Solution()
root = TreeNode.fromList([1,2,3,4,5,'#',6,7,'#','#','#','#',8])
s.connect(root)