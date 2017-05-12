__author__="fafu"
#coding=utf-8
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        if A is None or target is None:
            return 0
        if len(A) == 0:
            return 1
        if len(A) == 1:
            if A[0]>=target:
                return 0
            else:
                return 1
        low ,high = 0,len(A)-1
        while low<=high:
            if low == high:
                if A[low]==target:
                    return low
                elif A[low]<target:
                    return low+1
                else:
                    return low
            mid = low + ((high-low)>>1)
            if A[mid]==target:
                return mid
            elif A[mid]>target:
                high = mid -1
            else:
                low = mid+1
        return low
if __name__=="__main__":
    s = Solution()
    a = [1,3,5,6]
    print a
    # print s.searchInsert(a,5)
    # print s.searchInsert(a,2)
    # print s.searchInsert(a,7)
    # print s.searchInsert(a,0)
    print s.searchInsert([1],0)
            
