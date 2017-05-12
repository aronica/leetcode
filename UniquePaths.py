class Solution:
    def uniquePaths(self, m, n):
        if m == 1:
            return 1
        if n == 1:
            return 1
        dp = {(0,i):1 for i in xrange(n)}
        dp2 = {(j,0):1 for j in xrange(m)}
        dp.update(dp2)
        for i in xrange(1,m):
            for j in xrange(1,n):
                dp[(i,j)] = dp[(i-1,j)] + dp[(i,j-1)]
        return dp[(m-1,n-1)]

print __name__
if __name__ == "__main__":
    s = Solution()
    print s.uniquePaths(5,6)
    print s.uniquePaths(3,3)
        
    