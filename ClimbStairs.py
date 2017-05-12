__author__ = 'fafu'
class Solution:
    #Fibonacci
    def climbStairs(self, n):
        if n is None or n==0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        f1 = 1;f2 = 2;f3 = None
        i = 3
        while i <= n:
            f3 = f1 + f2
            f1 = f2
            f2 = f3
            i += 1
        return f3
