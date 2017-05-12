__author__ = 'fafu'
import math

class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            if n == 0:
                return 0
            return 1
        decimal = len(str(n))
        power = int(math.pow(10, decimal-1))
        remainder = n % power
        val = n / power
        if val > 1:
            return self.countDigitOne(power - 1)*(val-1) + power + self.countDigitOne(remainder) + remainder
        return self.countDigitOne(remainder) + remainder + self.countDigitOne(power - 1)

if __name__=="__main__":
    s = Solution()
    print s.countDigitOne(19)#1 10 11 12
    print s.countDigitOne(99)
    print s.countDigitOne(100)
    print s.countDigitOne(999)
    print s.countDigitOne(111)


