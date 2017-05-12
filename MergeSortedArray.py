__author__ = 'fafu'
class Solution:
    #Merge Sorted Array
    def merge(self, A, m, B, n):
        indexa = m-1
        indexb = n-1
        i = 0
        while indexa >= 0 and indexb>=0:
            if B[indexb]>A[indexa]:
                A[indexa+indexb+1] = B[indexb]
                indexb -= 1
            else:
                A[indexa+indexb+1] = A[indexa]
                indexa -= 1
        while indexb >= 0:
            A[indexb] = B[indexb]
            indexb -= 1
        return A
