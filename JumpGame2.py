class Solution:
    max_val = pow(2,31)
    def jump(self, A):
        if A is None or len(A) == 0 or len(A)==1 or A[0]==len(A)-1:
            return 0
        if A[0]==0:
            return -1
        li = {0:0}
        li.update({(1+i):1 for i in xrange(A[0])})
        for i in xrange(1,len(A)-1):
            if A[i] == 0:
                continue
            for j in xrange(1,min(A[i]+1,len(A)-i)):
                if i+j in li:
                    li[i+j] = min(li[i+j],li[i]+1)
                else:
                    li[i+j] = li[i]+1
        if len(A)-1 in li:
            return li[len(A)-1]
        return -1
if __name__=="__main__":
    s = Solution()
    s.jump([1,1,1,2,1])
                
            
            
            
            
        


    