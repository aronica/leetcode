__author__ = 'fafu'
class Solution:
    def sqrt(self, x):
        if x is None:
            return None
        if x <0:
            return None
        if x==0:
            return 0
        if x==1:
            return 1
        small = 1
        big = x
        while big-small>1:
            mid = (small+big)/2
            val = mid*mid
            if val<x:
                small = mid
            elif val>x:
                big = mid
            else:
                return mid
        if big == small:
            return small
        smalls = small*small
        bigs = big*big
        return float(x-smalls)/x < float(bigs-x)/x and small or big
