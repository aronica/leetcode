__author__ = 'fafu'
class Solution:
    def combine(self, n, k):
        return self.__combine__(1,n,k)

    def __combine__(self,start,end,k):
        if end-start+1 is None or k is None:
            return []
        if k == 1:
            return [[i] for i in xrange(start,end+1)]
        if end-start+1<k:
            return []
        if end-start+1 == k:
            return [[i for i in xrange(start,end+1)]]
        result = []
        res1 = self.__combine__(start+1,end,k-1)
        for i in res1:
            i.insert(0,start)
        res2 = self.__combine__(start+1,end,k)
        res1.extend(res2)
        return res1

