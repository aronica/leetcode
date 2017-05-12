import types


class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        if nums is None or len(nums) == 0 or k is None or type(k) is not types.IntType or k <= 0: return
        lens = len(nums)
        k = k % lens
        i , j = 0 , 0
        pre = nums[i]
        idx = (i + k) % lens
        for j in xrange(lens):
            tmp = nums[idx]
            nums[idx] = pre
            pre = tmp
            if idx==i:
                i+=1
                pre = nums[i]
                idx = i
            idx = (idx + k) % lens

if __name__ == "__main__":
    s = Solution()
    num = [1]
    s.rotate(num, 1)
    print num