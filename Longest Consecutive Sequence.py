__author__ = 'fafu'
class Solution:
    #longest consecutive sequence
    def longestConsecutive(self, num):
        if num is None:
            return 0
        if len(num) == 1:
            return 1
        dic = {i:False for i in num}
        maxnum = 1
        for i in num:
            if dic[i]:
                continue
            less = i-1
            count = 1
            while less in dic:
                dic[less] = True
                less -= 1
                count += 1
            less = i+1
            while less in dic:
                dic[less] = True
                less += 1
                count += 1
            if count>maxnum:
                maxnum = count
        return maxnum
