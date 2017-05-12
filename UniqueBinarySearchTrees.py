__author__ = 'fafu'
class Solution:
    # @return an integer
    def numTrees(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [1,1,2]
        for i in xrange(3,n+1):
            if i%2 == 1:
                sum = 0
                for j in xrange(i/2):
                    sum += 2*dp[i-1-j]*dp[j]
                sum += dp[i/2]*dp[i/2]
                dp.append(sum)
            else:
                sum = 0
                for j in xrange(i/2):
                    sum += 2*dp[i-1-j]*dp[j]
                dp.append(sum)
        return dp[-1]
s = Solution()
print s.numTrees(3)
print s.numTrees(4)
print s.numTrees(5)
print s.numTrees(6)




