__author__ = 'fafu'
class Solution:
    #Longest Palindromic Substring
    def longestPalindrome(self, s):
        if s is None or len(s) == 0 or len(s) ==1 :
            return s
        if len(s) == 2:
            return s[0] == s[1] and s or s[0]
        maxlen = 1
        length = len(s)
        i = 1
        dp =  [[False for x in xrange(length)] for x in xrange(length)]
        if s[0] == s[1]:
            maxlen = 2
            dp[0][1] = True
        dp[0][0] = True
        dp[1][1] = True

        for i in xrange(2,len(s)):
            dp[i][i] = True
            if maxlen == 1:
                if s[i-1] == s[i]:
                    dp[i-1][i] = True
                    if maxlen<2:
                        maxlen = 2
            index = (i - maxlen/2) == i and i-1 or i-maxlen/2
            for j in xrange(index,0,-1):

                if dp[j][i-1] and s[j-1]==s[i]:
                    dp[j-1][i] = True
                    if i+1-j+1>maxlen:
                        maxlen = i-j+2
        return maxlen

