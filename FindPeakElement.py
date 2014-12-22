__author__ = 'fafu'
class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        def __find__(num,start,end):
            if end - start == 0:
                if end == len(num)-1 or start == 0:
                    return start
                if num[start]>num[start-1] and num[start]>num[start+1]:
                    return start
                return -1
            if end - start == 1:
                if num[end]>num[start]:
                    if end == len(num)-1 or num[end]>num[end+1]:
                        return end
                if num[end]<num[start]:
                    if start == 0 or num[start]>num[start-1]:
                        return start
                return -1
            if end - start == 2:
                if num[start]>num[start+1]:
                    if start == 0 or num[start]>num[start-1]:
                        return start
                if num[start+1]<num[end]:
                    if end == len(num)-1 or num[end]>num[end+1]:
                        return end
                if num[start]<num[start+1] and num[start+1]>num[start+2]:
                    return start+1
                return -1
            low ,high = start, end
            while low<=high:
                mid = low + ((high - low)>>1)
                if mid == high and num[mid]>num[mid-1]:
                    return mid
                if mid == low and num[mid]>num[mid+1]:
                    return mid
                if num[mid]>num[mid-1] and num[mid]>num[mid+1]:
                    return mid
                else:
                    index = __find__(num,start,mid)
                    if index != -1:
                        return index
                    index = __find__(num,mid,end)
                    if index != -1:
                        return index
                    return -1
            return -1
        return __find__(num,0,len(num)-1)

if __name__=="__main__":
    s = Solution()
    print s.findPeakElement([1,3,2,1,2,1])


