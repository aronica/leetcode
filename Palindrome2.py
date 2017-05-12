__author__ = 'fafu'
import time
class Solution:
    def partition(self, s):
        length = len(s)
        if s is None or length<1:
            return 0
        if length == 1:
            return 0
        if length == 2:
            if s[0] == s[1]:
                return 0
            else:
                return 1
        dp = []

        for i in xrange(length):
            dp.append(set([i]))
        if s[0] == s[1]:
            dp[1].add(0)


        for i in xrange(2,length):
            for j in dp[i-1]:
                if j>0 and s[j-1]==s[i]:
                    dp[i].add(j-1)
            if s[i-1]==s[i]:
                dp[i].add(i-1)

        maxlen = self.dfs_q(dp,s)
        return maxlen

    def dfs_q(self,dp,s):
        index = len(s)-1
        se = dp[index]
        count = 0
        while 0 not in se:
            se2 = set()
            for i in se:
                se2 = se2.union(dp[i-1])
            count += 1
            se = se2
        return count







print "yes"
s = Solution()
time.clock()
print s.partition("apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp")
print time.clock()
print "no"
