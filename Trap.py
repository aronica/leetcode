class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        if A is None or len(A)<2:
            return 0
        cumulated = 0

        a ,b = len(A)-2,len(A)-1
        while a>=0 and A[a]>=A[b]:
            a -= 1
            b -= 1
        length = b+1
        if a==-1:
            return 0
        maxes = {a:b}
        a -= 1
        while a>=0:
            if A[a]>=A[maxes[a+1]]:
                maxes[a] = a
            else:
                maxes[a] = maxes[a+1]
            a -= 1
        x,y,z = 0,1,0
        #A[y]<A[x],x = max1
        while z<length:
            while y<len(A) and A[y]>=A[x]:
                x=y
                y+=1
            if x == length:
                return cumulated
            z = x+2
            y = x+1
            found = False
            while z<length and A[z]<=A[y]:
                y = z
                z += 1
            if z >= length:
                break
            found = True
            # y = min
            if A[maxes[y]]>=A[x]:
                m = x+1
                top = A[x]
                while m<maxes[y] and A[m]<top:
                    cumulated += max(top-A[m],0)
                    m += 1
                x = m
                continue
            else:#A[maxes[y]]<A[x]
                m = x+1
                top = A[maxes[y]]
                while m<maxes[y]:
                    cumulated += max(top-A[m],0)
                    m += 1
                x = m
                continue
        return cumulated
if __name__=="__main__":
    s = Solution()
    a = [0,3,0,4,8,4,6,9,0,3,2]
    print a
    print s.trap(a)





