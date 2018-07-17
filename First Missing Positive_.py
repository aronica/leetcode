"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""
__author__ = 'fafu'


class Solution:
    def firstMissingPositive(self, nums):
        i, n = 0, len(nums)
        while i < n:
            if nums[i] > 0 and nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                # swap
                temp = nums[i]
                nums[i] = nums[nums[i] - 1]
                nums[temp - 1] = temp
            else:
                i += 1
        for i, v in enumerate(nums):
            if v != i + 1:
                return i + 1
        return n + 1
nums=[3,4,-1,1]
s = Solution()
s.firstMissingPositive(nums)