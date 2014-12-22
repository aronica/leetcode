__author__ = 'fafu'
class Solution:
    def isScramble(self, s1, s2):
        if s1 is None or s2 is None:
            return False
        if s1 == s2:
            return True
        if s1[0] == s2[0]:
            return self.isScramble(s1[1:],s2[1:])
        else:
            pass

