__author__ = 'fafu'
class Solution:
    #we can do the transaction multiple times
    def maxProfit2(self, prices):
        if prices is None or len(prices)==0:
            return 0
        if len(prices) == 2:
            return max(0,prices[1]-prices[0])
        dp = (0,-prices[0])   #resource 1,0
        for i in xrange(1,len(prices)):
            resource1 = max(dp[0],prices[i]+dp[1])#you
            resource0 = max(dp[1],dp[0]-prices[i])#meiyou
            dp = (resource1,resource0)
        return max(dp[0],dp[1])
