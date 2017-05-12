__author__ = 'fafu'


class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        result = [[0 for i in xrange(n)] for j in xrange(n)]
        i,j = 0,0
        index = 1
        cycle = 0
        while index<=n*n:
            edge = n - cycle
            while j<edge:
                result[i][j] = index
                index += 1
                j += 1
            j -= 1
            i += 1
            edge = n - cycle
            while i<edge:
                result[i][j] = index
                index += 1
                i += 1
            i -= 1
            j -= 1
            edge = cycle-1
            while j>edge:
                result[i][j] = index
                index += 1
                j -= 1
            i -= 1
            j += 1
            edge = cycle
            while i>cycle:
                result[i][j] = index
                index += 1
                i -= 1
            i += 1
            j += 1
            cycle += 1
        return result
if __name__=="__main__":
    s = Solution()
    res = s.generateMatrix(4)
    for i in res:
        print i




