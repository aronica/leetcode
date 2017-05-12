__author__ = 'fafu'
class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if A is None or len(A)<3:
            return A is None and 0 or len(A)
        cursor = A[0]
        cnt = 1
        i = 1
        dup = 0
        while i<len(A):
            if A[i] == cursor and cnt == 1:
                cnt = 2
                if dup>0:
                    A[i-dup] = A[i]
            elif A[i] == cursor and cnt > 1:
                dup += 1
            elif A[i] != cursor:
                cursor = A[i]
                cnt = 1
                if dup>0:
                    A[i-dup] = A[i]
            i += 1
        return len(A) - dup
s = Solution()
a = [1,1,1,2,3,3,3]
print s.removeDuplicates(a),a


