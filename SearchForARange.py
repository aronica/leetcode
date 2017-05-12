__author__ = 'fafu'
class Solution:
    def searchRange(self, A, target):
        left = 0;right = len(A)-1
        while left<=right:
            mid = left + ((right - left)>>2)
            if A[mid]<target:
                left = mid + 1
            elif A[mid]>target:
                right = mid - 1
            else:
                nmid = mid
                nmid2 = mid
                while nmid>-1 and A[nmid]==target:
                    nmid -= 1
                while nmid2<len(A) and A[nmid2]==target:
                    nmid2 += 1
                return [nmid+1,nmid2-1]
        return [-1,-1]
s = Solution()
print s.searchRange([5, 7, 7, 8, 8, 10],5)
