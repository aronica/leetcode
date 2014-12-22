__author__ = 'fafu'
class Solution:
    def sortColors(self, A):
        if A is None or len(A)<2:
            return A
        i,j,m = 0,len(A)-1,0
        while i<j:
            while i<=j and A[i] == 0:
                i += 1
            while i<=j and A[j]==2:
                j -= 1
            if i >= j:
                break
            if A[i]>A[j]:
                tmp = A[j]
                A[j] = A[i]
                A[i] = tmp
            elif A[i] == A[j]: #both 1
                found = False
                for m in xrange(i+1,j):
                    if A[m] == 0:
                        found = True
                        A[m] = A[i]
                        A[i] = 0
                        i += 1
                        break
                    elif A[m] == 2:
                        found = True
                        A[m] = A[j]
                        A[j] = 2
                        j -= 1
                        break
                if not found:
                    return
s = Solution()
a = [0,0]
s.sortColors(a)
print a






