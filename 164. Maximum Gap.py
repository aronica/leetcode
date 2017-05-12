import math
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums)<2:
            return 0
        minv,maxv = min(nums),max(nums)
        s = set(nums)
        if len(s)==1:
            return 0
        gap = int(math.ceil((maxv - minv+1)*1.0/len(nums)))
        if gap == 0:
            return 0
        val = [(None,None) for i in xrange(len(nums))]
        for i in nums:
            index = int(math.floor((i-minv)*1.0/gap))
            minvalue,maxvalue = val[index]
            if minvalue is None or minvalue>i:
                minvalue = i
            if maxvalue is None or maxvalue<i:
                maxvalue = i
            val[index] = (minvalue,maxvalue)
        maxgap = -1
        i ,j = 0 ,1
        while j<len(nums):
            if val[j][0] is None:
                j += 1
            else:
                if val[j][0] - val[i][1]>maxgap:
                    maxgap = val[j][0] - val[i][1]
                i = j
                j += 1
        return maxgap