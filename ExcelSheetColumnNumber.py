__author__ = 'fafu'
from ExcelColumnTitle import Solution as ss;
class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        if s is None or len(s) == 0:
            return None
        dic = {chr(i+ord('A')):i+1 for i in xrange(0,26)}
        total = 0
        lens = len(s)
        for i in xrange(lens):
            total += dic[s[lens-i-1]]*pow(26,i)
        return total
if __name__=="__main__":
    s = Solution()
    an = ss()
    print s.titleToNumber("AA")
    print s.titleToNumber("Z")
    print 3344,s.titleToNumber(an.convertToTitle(3344))




