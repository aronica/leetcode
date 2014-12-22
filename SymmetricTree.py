__author__ = 'fafu'
class Solution:
    def isSymmetric(self, root):
        if root is None:
            return False
        #return self.__isSymmetric(root.left,root.right)
        return self.__isSymmetricNoneRecursively(root)


    def __isSymmetric(self,first,second):
        if first is None and second is None:
            return True
        result = first is not None and second is not None
        if not result:
            return False
        if first.val != second.val:
            return False
        rel1 = self.__isSymmetric(first.left,second.right)
        rel2 = self.__isSymmetric(first.right,second.left)
        return rel1 and rel2

    def __isSymmetricNoneRecursively(self,root):
        first = root.left
        second = root.right
        stack = list()
        stack.append((first,second))
        while len(stack)>0:
            first,second = stack.pop()
            if first is None and second is None:
                continue
            result = first is not None and second is not None
            if not result:
                return False
            if first.val != second.val:
                return False
            stack.append((first.left,second.right))
            stack.append((first.right,second.left))
        return True
