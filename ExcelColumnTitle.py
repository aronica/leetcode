__author__ = 'fafu'
class Solution:
    # @return a string
    def convertToTitle(self, num):
        if num is None:
            return None
        li = [chr(i+ord('A')) for i in xrange(0,26)]
        result = []
        while num/26>0:
            val = num%26
            if val == 0:
                result.insert(0,"Z")
                num = num/26-1
            else:
                result.insert(0,li[val-1])
                num /=26
        if num>0:
            result.insert(0,li[num-1])
        return "".join(result)

if __name__=="__main__":
    s = Solution()
    print 26,s.convertToTitle(26)
    print 27,s.convertToTitle(27)
    print 26*26,s.convertToTitle(26*26)
    print 26*26+1,s.convertToTitle(26*26+1)