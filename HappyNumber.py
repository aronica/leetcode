class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        while n != 1 and n not in s:
            s.add(n)
            n = self.calc(n)
        if n == 1:
            return True
        else:
            return False
    def calc(self,n):
        return reduce(lambda x,y: x+ y*y,[int(i) for i in str(n)],0)

if __name__=="__main__":
    s = Solution()
    print s.isHappy(19)
