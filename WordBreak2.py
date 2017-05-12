__author__ = 'fafu'
class Solution:
    def wordBreak(self,s,dict):
        if s is None or len(dict) == 0:
            return []
        if s in dict and len(s)==1:
            return [s]
        dp = { -1:True }
        ran = {-1:[]}
        for i in xrange(0,len(s)):
            for j in xrange(0,i+1):
                str = s[i-j:i+1]
                if str in dict and dp[i-j-1]:
                    dp[i] = True
                    if i-j not in ran:
                        ran[i-j] = [i]
                    else:
                        ran[i-j].append(i)
            dp[i] = i in dp or False

        if dp[len(s) -1]:
            result = []
            self.dfs(ran,0,"",result,s)
            return result
        return []

    def dfs(self,ran,index,tmp,result,s):
        if index in ran and ran[index] is not None:
            lens = len(tmp)
            for i in ran[index]:
                tmp +=  s[index:i+1] +" "
                if i == len(s)-1:
                    result.append(tmp.strip())
                else:
                    self.dfs(ran,i+1,tmp,result,s)
                tmp = tmp[0:lens]


s = Solution()
print s.wordBreak("abcd", ["a","abc","b","cd"])
print s.wordBreak("catsanddog",["cat", "cats", "and", "sand", "dog"])


