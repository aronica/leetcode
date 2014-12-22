__author__ = 'fafu'
class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        ele = num[0]
        count = 1
        j = 1
        while j<len(num):
            if num[j] == ele:
                count += 1
                if count>len(num)/2:
                    return ele
            else:
                count -= 1
                if count == 0:
                    ele = num[j]
                    count = 1
            j += 1
        return ele
if __name__=="__main__":
    s = Solution()
    print s.majorityElement([1,1,2,2,3,3,4,4,3,3,3,3])



