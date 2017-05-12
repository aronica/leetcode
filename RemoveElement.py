__author__ = 'fafu'
class Solution:
    #Remove Element
    def removeElement(self, A, elem):
        if A is None or elem is None: return 0
        if len(A) == 1:
            if A[0] == elem:
                return 0
            else:
                return 1
        i = 0
        last = len(A) - 1
        while i <= last:
            if A[i] == elem:
                while i<= last and A[last] == elem:
                    last -= 1
                    A.pop()
                if i < last:
                    A[i] = A[last]
                    A.pop()
                    last -= 1
            i += 1
        return last + 1
