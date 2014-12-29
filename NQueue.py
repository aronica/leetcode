__author__ = 'fafu'
import time
class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        def __calc__(tmp,tmpre,result,index):
            lens = len(tmp)
            for i in xrange(n):
                if i not in tmp and (len(tmp)==0 or abs(tmp[-1]-i)!=1):
                    tmp.append(i)
                    li = []
                    for m in xrange(i):
                        li.append(".")
                    li.append("Q")
                    for m in xrange(i+1,n):
                        li.append(".")
                    tmpre.append("".join(li))
                    if index+1==n:
                        result.append(tmpre)
                    else:
                        __calc__(tmp,tmpre,result,index+1)
                tmp = tmp[0:lens]
                tmpre = tmpre[0:lens]
        if n<4:
            return []
        result = []
        __calc__([],[],result,0)
        newresult = []
        return newresult
if __name__=="__main__":
    s = Solution()
    time.clock()
    s.solveNQueens(9)
    print time.clock()





