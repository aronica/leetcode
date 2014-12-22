__author__ = 'fafu'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
    @staticmethod
    def fromList(l):
        if l is None or len(l)==0:
            return None
        stack = list([TreeNode(l[0])])
        root = stack[0]
        node = None
        for i in xrange(1,len(l)):
            if node is None:
                node = stack.pop(0)
                if l[i]!='#':
                    newnode = TreeNode(int(l[i]))
                    node.left = newnode
                    stack.append(newnode)
                elif i!= len(l)-1:
                    node.left = None
            else:
                if l[i]!='#':
                    newnode = TreeNode(int(l[i]))
                    node.right = newnode
                    stack.append(newnode)
                    node = None
                elif i!= len(l)-1:
                    node.right = None
                    node = None
        return root
    @staticmethod
    def toStr(root):
        if root is None:
            return None
        if root.left is None or root.right is None:
            return root.val
        stack = list([root])
        node = root
        s = list([str(root.val)])
        while len(stack)>0:
            node = stack.pop(0)
            #s.append(node.val)
            if node.left is not None:
                stack.append(node.left)
                s.append(str(node.left.val))
            elif len(stack)>0:
                s.append("#")
            if node.right is not None:
                stack.append(node.right)
                s.append(str(node.right.val))
            elif len(stack)>0:
                s.append("#")
        for i in xrange(len(s)-1,0,-1):
            if s[i] == "#":
                s.pop()
            else:
                break
        return " ".join(s)

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def print_linkedlist(node):
    stack = list()
    while node is not None:
        stack.append(str(node.val))
        node = node.next
    print "->".join(stack)


if __name__=="__main__":
    root = TreeNode.fromList([1,-2,-3,1,3,-2,'#',-1])
    print TreeNode.toStr(root)






