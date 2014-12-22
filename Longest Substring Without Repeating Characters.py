__author__ = 'fafu'
class Solution:
    def lengthOfLongestSubstring(self, s):
        if s is None:
            return 0
        if len(s)==1:
            return 1
        dic = {}
        maxcount = 1
        count = 0
        startindex = 0
        for index,i in enumerate(s):
            if i not in dic:
                count += 1
                dic[i] = index
            else:
                idx = dic[i]
                oldstartindex = startindex
                while startindex<idx:
                    del dic[s[startindex]]
                    startindex += 1
                dic[i] = index
                startindex = idx+1
                count -= startindex - oldstartindex - 1
            if count>maxcount:
                maxcount = count
        return maxcount
