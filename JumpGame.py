#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "fafu"
import time
class Solution:
    def canJump(self, A):
        if A is None or len(A) == 0 or len(A)==1 or A[0]==len(A)-1:
            return True
        dic = dict()
        if A[0]>=len(A)-1:
            return True
        foundvalid = False
        for i in xrange(len(A)-1):
            val = A[i]
            if i + val>=len(A)-1:
                dic[i] = False
                foundvalid = True
            elif val == 0:
                dic[i] = True
            else:
                found = False
                for m in xrange(val):
                    if i+m<len(A)-1 and A[i+m] != 0:
                        found = True
                        break
                if not found:
                    dic[i] = True
        if not foundvalid:
            return False
        return self.__jump__(A,0,dic)

    def __jump__(self,A,index,dic):
        val = A[index]
        if val == 0 or index in dic and dic[index]:
            return False
        #if index in dic and dic[]if index in dic and dic[]
        if (index+val) in dic and not dic[index+val] or index+val>=len(A)-1:
            return True
        # if val == 1 and dic[index+1]:
        #     dic[index] = True
        #     return False
        for j in xrange(val,0,-1):
            if A[index+j] == 0:
                continue
            if self.__jump__(A,index+j,dic):
                return True
        dic[index] = True
        return False

if __name__=="__main__":
    s = Solution()
    a = [2,3,1,1,4]
    print time.clock()
    a = [0, 1]
    print s.canJump(a)

    print a,s.canJump(a)
    print time.clock()
    b = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
    print b,s.canJump(b)
    print time.clock()
    b=[i for i in xrange(25000,0,-1)]
    b.append(3)
    b.append(3)
    b.append(3)
    print s.canJump(b)
    print time.clock()
