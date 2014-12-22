__author__ = 'fafu'
class Solution:
    #Container With Most Water
    def maxArea(self, height):
        if height is None or len(height) < 2:
            return 0
        max_water = 0
        dp = [[] for i in xrange(len(height))]

        dp[1] = 0

        for i in xrange(2,len(height)-1):
            maxval = 0
            dp[i] = 0
            for j in xrange(i):
                if height[i]>height[j] or (height[i]<height[j] and height[i]>height[dp[j]]):
                    val1 =  (i - dp[j]) * min(height[i],height[dp[j]])
                    val2 = (i-j)*min(height[i],height[j])
                    if val1>=val2 and val1>maxval:
                        dp[i] = dp[j]
                        max_water = max(val1,max_water)
                    else:
                        if val2>maxval:
                            dp[i] = j
                        max_water = max(val2,max_water)
                else:
                    val = (i - dp[j])*height[i]
                    if val>maxval:
                        dp[i] = dp[j]
                        max_water = max(val,max_water)
        return max_water
