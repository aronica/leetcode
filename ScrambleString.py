__author__ = 'fafu'
class Solution:
    def isScramble(self, s1, s2):
        if s1 is None or s2 is None:
            return False
        if len(s1)!= len(s2):
            return False
        dica = dict()
        dicb = dict()
        for i in s1:
            if i in dica:
                dica[i] = dica[i]+1
            else:
                dica[i] = 1
        for i in s2:
            if i in dicb:
                dicb[i] = dicb[i]+1
            else:
                dicb[i] = 1
        if dica!=dicb:
            return False






