__author__ = 'fafu'
class Solution:
    # @return a string
    def getPermutation(self, n, k):
        if n == 1:
            return "1"
        count = [1]
        for i in xrange(2,n):
            count.append(count[-1]*i)
        if k>count[-1]*n:
            return None
        letter = "123456789"[0:n]
        i = 0
        res = ""
        remainer = k-1
        while i<n and n-2-i>=0:
            result = remainer/count[n-2-i]
            remainer = remainer%count[n-2-i]
            res += letter[result]
            if result == len(letter)-1:
                letter = letter[0:-1]
            else:
                letter = letter[0:result] + letter[result+1:]
            i += 1
        return res +letter
if __name__=="__main__":
    s = Solution()
    print s.getPermutation(3,1)
    print s.getPermutation(3,6)
    print s.getPermutation(3,5)
    print s.getPermutation(3,4)
    print s.getPermutation(3,3)
    print s.getPermutation(3,2)



