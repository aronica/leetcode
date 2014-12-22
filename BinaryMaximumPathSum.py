__author__ = 'fafu'
from Meta import TreeNode
class Solution:
    def maxPathSum(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.val
        maximum = root.val
        node = root
        stack = list()
        sums = None
        while node is not None or len(stack)>0:
            if node is not None:
                if node.left is not None:
                    stack.append((node,None,None,None))
                    node = node.left
                elif node.right is not None:
                    stack.append((node,'none',None,None))
                    node = node.right
                else:
                    maximum = max(node.val,maximum)
                    sums = node.val
                    node = None

            else:
                node,left,right,val = stack.pop()
                if left is None:
                    left = sums
                    stack.append((node,left,None,None))
                    node = node.right
                    sums = None
                    continue
                elif right is None:
                    if sums is not None:
                        right = sums
                    if left == 'none' and right is not None:
                        maximum = max(maximum,right,node.val,right+node.val)
                        sums = max(node.val,node.val+right)
                    elif left == 'none' and right is None:
                        maximum = max(maximum,node.val)
                        sums = node.val
                    elif right is not None:
                        maximum = max(maximum,left,right,left+node.val,right+node.val,left+right+node.val)
                        sums = node.val
                        if node.val+left>sums:
                            sums = node.val+left
                        if node.val+right>sums:
                            sums = node.val+right
                        if node.val + left + right>sums:
                            sums = node.val + left + right

                    else:
                        maximum = max(maximum,left,node.val,left+node.val)
                        sums = max(node.val,node.val+left)
                node = None
        return maximum

root = TreeNode.fromList([-2,-1])
s = Solution()
print s.maxPathSum(root)