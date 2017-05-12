__author__ = 'fafu'


class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        if s is None or len(s) < 2: return 0
        maxlen = 0
        num, start = 0, 0
        dp = {}
        # (())(()))(((())))
        for i in xrange(1, len(s)):
            if s[i] == ")":
                if i == 1:
                    if s[0] == "(":
                        dp[i] = 0
                        maxlen = max(maxlen,2)
                else:
                    if s[i-1]=="(":
                        dp[i] = i-1
                        maxlen = max(maxlen,2)
                        if i-2 in dp:
                            dp[i] = dp[i-2]
                            maxlen = max(maxlen,i-dp[i]+1)
                    else:#s[i-1]==")"
                        if i-1 in dp:
                            if dp[i-1]>0:
                                if s[dp[i-1]-1]=="(":
                                    dp[i] = dp[i-1]-1
                                    if dp[i]-1 in dp:
                                        dp[i] = dp[dp[i]-1]
                                    maxlen = max(maxlen,i-dp[i]+1)
        return maxlen


if __name__ == "__main__":
    s = Solution()
    print s.longestValidParentheses("(()))((())((())((()))))")



