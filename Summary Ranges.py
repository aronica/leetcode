__author__ = 'fafu'
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        return self.__summary__(nums, [], 0)

    def __summary__(self, nums, pre, index):
        if nums is None or len(nums)-index == 0:
            return pre
        if len(nums)-index == 1:
            pre.extend([str(nums[index])])
            return pre
        last = nums[index]
        start = last
        end = last
        for i in xrange(index+1, len(nums)):
            if nums[i] == last + 1:
                last = end = nums[i]
                if i == len(nums)-1:
                    pre.append(str(start)+"->"+str(last))
                    return pre
            else:
                current = str(start)
                if start != end:
                    current = str(current) + "->" + str(end)
                pre.append(current)
                return self.__summary__(nums, pre, i)

if __name__=="__main__":
    s = Solution()
    print s.summaryRanges([1,2,3,7,9])
    print s.summaryRanges([1,2,3,7,8,9])
    print s.summaryRanges([1,2,3,7,9,11,12])