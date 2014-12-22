class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        if num is None or len(num)<2:
            return num
        if len(num) == 2:
            num.reverse()
            return num
        m,n = len(num)-2,len(num)-1
        while num[m]>=num[n] and m>=0:
            m -= 1
            n -= 1
        if m!=-1:
            n = len(num)-1
            while num[n]<=num[m]:
                n -= 1
            tmp = num[m]
            num[m] = num[n]
            num[n]=tmp
            #reverse index>m
            i,j = m+1,len(num)-1
            while i<j:
                tmp = num[i]
                num[i] = num[j]
                num[j] = tmp
                i += 1
                j -= 1
            return num
        else:
            num.reverse()
            return num
if __name__=="__main__":
    s = Solution()
    a = [1,2,3]
    print s.nextPermutation(a)
    a = [3,2,1]
    print s.nextPermutation(a)
    a = [1,1,5]
    print s.nextPermutation(a)
    
        
            
            
        