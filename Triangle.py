__author__ = 'fafu'
class Solution:
    def minimumTotal(self, triangle):
        if triangle is None or len(triangle)==0:
            return 0
        if len(triangle)==1:
            return triangle[0][0]
        dp = [triangle[0][0]]
        for i in xrange(1,len(triangle)):
            dp.append(dp[-1]+triangle[i][-1])
            for j in xrange(len(triangle[i])-2,0,-1):
                dp[j] = min(dp[j-1],dp[j])+triangle[i][j]
            dp[0] = dp[0]+triangle[i][0]
        return min(dp)
s = Solution()
print s.minimumTotal([
    [2],
    [3,4],
    [6,5,7],
    [4,1,8,3]
])



