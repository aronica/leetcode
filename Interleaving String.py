__author__ = 'fafu'
class Solution:
    #Interleaving String
    def isInterleave(self, s1, s2, s3):
        if s1 is None or s2 is None or s3 is None or len(s1)+len(s2)!=len(s3):
            return False
        m = 0;n=0;k = 0;nn = False
        dp = []
        while m<len(s1) and n<len(s2) and m+n < len(s3)-1:
            if s1[m] == s3[m+n] and s2[n] == s1[m]:
                m += 1
                dp.append((m,n))
            elif s1[m] == s3[m+n]:
                m += 1
            elif s2[n] == s3[m+n]:
                n += 1
            else:
                while len(dp)>0 and not dp[-1]:
                    n -= 1
