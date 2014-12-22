__author__ = 'fafu'
class Solution:
    #Longest Common Prefix
    def longestCommonPrefix(self, strs):
        if strs is None or len(strs)==0:
            return None
        if len(strs)==1:
            return strs[0]
        maxs =  min(len(i) for i in strs)
        prefix = ""
        length = len(strs)
        i = 1
        while i<length:
            a = strs[i]
            b = strs[i - 1]
            while a[0:maxs] != b[0:maxs]:
                maxs -= 1
            if maxs == 0:
                break
            i += 1
        if maxs == 0:
            return ""
        return strs[0][0:maxs]
