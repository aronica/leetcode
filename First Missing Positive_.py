__author__ = 'fafu'
class Solution:
    def firstMissingPositive(self, A):
        if A is None or len(A)==0 or len(A)==1 and A[0]==0:
            return 1
        if len(A)==1 and len(A)==1:
            return 2
        elif len(A)==1 and len(A)>1:
            return len(A)-1

        minval = None
        maxval = 0
        j = len(A)-1
        i = 0
        while i<=j:
            while A[j]<=0:
                j-= 1
            if A[i]<=0:
                tmp = A[j]
                A[j] = A[i]
                A[i] = tmp
                j -= 1
            else:
                if minval is None or minval>A[i]:
                    minval = A[i]
                if A[i]>maxval:
                    maxval = A[i]
                i += 1

        if maxval-minval == j:
            if minval == 1:
                return maxval+1
            return minval-1
        if maxval==minval:
            if minval == 1:
                return maxval+1
            return minval-1
        i = 0
        newj = j
        while i<=j:
            if A[i]-minval==i:
                i+= 1
            elif A[i]-minval>i:
                tmp = A[i]
                idx= A[i]-minval
                if A[idx]>0:
                    A[i] = A[idx]
                else:
                    A[i] = None
                    i+=1
                A[idx]= tmp
        i = 0
        while i<=j:
            if A[i]!=i+minval:
                return i+minval
            i+=1