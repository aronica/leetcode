class Solution:
    def search(self, A, target):
        if A is None or target is None or len(A)==0:
            return False
        if len(A)==1:
            if A[0]!=target:
                return False
            return True
        return self.__getindex__(0,len(A)-1,A,target)
    
    def __getindex__(self,start,end,A,target):
        # if A[start]<A[end]:
        #     return self.__get__(start,end,A,target)
        mid = start + ((end-start)>>1)
        if mid == start:
            if A[start] == target:
                return True
            if A[end] == target:
                return True
        else:
            if A[start]<A[mid]:
                if A[start]<=target and A[mid]>= target:
                    return self.__get__(start,mid,A,target)
                else:
                    return self.__getindex__(mid,end,A,target)
            elif A[start]>A[mid]:
                if A[mid]<=target and A[end]>=target:
                    return self.__get__(mid,end,A,target)
                else:
                    return self.__getindex__(start,mid,A,target)
            else:# A[start]==A[mid]
                if A[start]==target:
                    return True
                else:
                    return self.__getindex__(mid+1,end,A,target) or self.__getindex__(start,mid-1,A,target)

        return False
                    
                    
    def __get__(self,start,end,A,target):
        low = start
        high = end
        while low<=high:
            mid = low + ((high-low)>>1)
            if A[mid] == target:
                return True
            elif A[mid]<target:
                low = mid+1
            else:
                high = mid -1
        return False
if __name__=="__main__":
    s = Solution()
    a = [4, 5, 6,6,7, 7, 0, 1,1, 2]
    print a
    print 8,s.search(a,8)
    print 5,s.search(a,5)
    print 1,s.search(a,1)
    print 0,s.search(a,0)
    print 6,s.search(a,6)
    print 3,s.search(a,3)
    a = [6,0,1,1,2,2,3,4,5]
    print a
    print 4,s.search(a,4)
    print 6,s.search(a,6)
    print 5,s.search(a,5)
    print 2,s.search(a,2)
    a = [2,3,4,5,5,0,1,2]
    print a
    print 1,s.search(a,1)
    print 3,s.search(a,3)
    print 0,s.search(a,0)
    print 5,s.search(a,5)
    a=[1,3,5,5,6,9]
    print a
    print 2,s.search(a,2)
    a=[1,3,1,1,1]
    print a
    print 3 ,s.search(a,3)

            
    
        