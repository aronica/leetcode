__author__ = 'fafu'
"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j
in the array such that nums[i] = nums[j] and the difference between i and j is at most k.
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if nums is None or len(nums) < 2:
            return False
        s = set(nums[0:k+1])
        if len(s)<k+1:
            if len(s)==len(nums):
                return False
            else:
                return True
        for i in xrange(k+1,len(nums)):
            s.remove(nums[i-k-1])
            s.add(nums[i])

            if len(s)<k+1:
                return True
        return False

if __name__=="__main__":
    s = Solution()
    print s.containsNearbyDuplicate([1,2,1,2,4,3],1)



