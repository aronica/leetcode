__author__ = 'fafu'
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a = 1
        while a<= n:
            if a^n == 0:return True
            a = a<<1
        return False
