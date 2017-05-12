__author__="fafu"
#charset=utf-8
class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):#m*n grid
        if grid is None or len(grid)==0 or len(grid[0])==0:
            return 0
        if len(grid)==1 and len(grid[0])==1:
            return grid[0][0]
        dp = {(0,0):grid[0][0]}
        m = len(grid)
        n = len(grid[0])
        for i in xrange(m):
            for j in xrange(n):
                if i == 0:
                    if j == 0:
                        continue
                    dp[(i,j)] = dp[(i,j-1)]+grid[i][j]
                elif j == 0:
                    dp[(i,j)] = dp[(i-1,j)]+grid[i][j]
                else:
                    dp[(i,j)] = min(dp[(i-1,j)],dp[i,j-1])+grid[i][j]
        return dp[(m-1,n-1)]
                
        
        
        