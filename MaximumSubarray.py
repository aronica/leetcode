class Solution:
    def maxSubArray(self, A):
        def __max__(a,start,end):
            if end-start==0:
                return (a[start],start,end)
            end1 = start + ((end-start)>>1)
            first , s1,e1= __max__(a,start,end1)
            second , s2,e2 = __max__(a,end1+1,end)
            maxval ,s,e= first,s1,e1
            if maxval<second:
                maxval,s,e = second,s2,e2
            #sums = sum(a[e1+1:s2])
            sums=A[s1]
            maxes = sums
            ss,ee=s1,e1
            for n in xrange(s1+1,e2+1):
                if sums<0:
                    sums = A[n]
                    ss = n
                else:
                    sums += A[n]
                if maxval<sums:
                    maxval,s,e = sums,ss,n
            return (maxval,s,e)
            
            
        if A is None:
            return None
        if len(A)==1:
            return A[0]
        return __max__(A,0,len(A)-1)[0]
        
        
    def maxSubArray2(self, A):
        if A is None:
            return None
        if len(A)==1:
            return A[0]
        maxval = max(A)
        sums = A[0]
        i = 1
        while i<=len(A)-1:
            if sums<0:
                sums = A[i]
            else:
                sums += A[i] 
            if maxval<sums:
                maxval = sums
            i += 1
        return maxval
if __name__=="__main__":
    s = Solution()
    a = [-2,-1]
    print a,s.maxSubArray(a)
    a = [-2,1,-3,4,-1,2,1,-5,4]
    print a,s.maxSubArray(a)
    
            
            
            