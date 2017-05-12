__author__ = 'fafu'
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        if num is None or len(num)==0:return []
        if len(num)==1:return [num]
        def __pop__(items,target):
            if len(items)==0:
                return [target]
            result = []
            for i in xrange(len(items)+1):
                item = []
                item.extend(items[0:i])
                item.append(target)
                item.extend(items[i:])
                result.append(item)
            return result
        res = [[num[0]]]
        for i in xrange(1,len(num)):
            res2 = []
            for j in res:
                res2.extend(__pop__(j,num[i]))
            res = res2
        return res
if __name__=="__main__":
    s = Solution()
    print s.permute([1,2,3,4])








