__author__ = 'fafu'
import time
class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        def __calc__(tmp,result,index,se):
            lens = len(tmp)
            for i in xrange(n):
                if i not in se and (len(tmp)==0 or abs(tmp[-1]-i)!=1):
                    tmp.append(i)
                    se.add(i)
                    if index+1==n:
                        result.append(tmp)
                    else:
                        __calc__(tmp,result,index+1,se)
                    se.discard(i)
                tmp = tmp[0:lens]
        if n<4:
            return []
        result = []
        __calc__([],result,0,set())
        newresult = []
        for i in result:
            res = [["." for m in xrange(n)] for a in xrange(n)]
            j = 0
            while j<n:
                res[j][i[j]]="Q"
                j+=1
            newresult.append(["".join(m) for m in res])
        return newresult
if __name__=="__main__":
    s = Solution()
    time.clock()
    s.solveNQueens(9)
    print time.clock()





