__author__ = 'fafu'
class Solution:
    #word break
    def wordBreak(self, s, dict):
        dic = set(dict)
        if s is None or len(dic) == 0:
            return False
        if s in dic:
            return True
        dp = {-1:True}
        for i in xrange(0,len(s)):
            for j in xrange(0,i+1):
                if s[i-j:i+1] in dict and dp[i-j-1]:
                    dp[i] = True
                    break
            dp[i] = i in dp or False

        return dp[len(s)-1]
