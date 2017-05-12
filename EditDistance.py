__author__ = 'fafu'
import time
class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        if word1 is None and word2 is None or word1 == word2:
            return 0
        if word1 is None or len(word1)==0:
            return len(word2)
        if word2 is None or len(word2)==0:
            return len(word1)

        dp = {(-1,-1):0,(-1,0):0,(0,-1):0} #Format:index of word1,steps
        i = 0
        j = 0
        while i<len(word2):
            for j in xrange(min(i+1,len(word1))):
                if word1[i] == word2[j]:
                    dp[(j,i)]=dp[(j-1,i-1)]
                else: #word1[i] != word2[j]:
                    dp[(j,i)]=min(dp[(j-1,i-1)]+1,dp[(j,i-1)]+1)
            i+=1



if __name__=="__main__":
    s = Solution()
    print time.clock()
    print s.minDistance("google","baidu")
    print time.clock()
    print s.minDistance("dinitrophenylhydrazine","acetylphenylhydrazine")
    print time.clock()




