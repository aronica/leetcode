class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s is None or t is None or len(s)!=len(s):
            return False
        sset = set(s)
        tset = set(t)
        if len(sset)!=len(tset):
            return False

        newdict = dict()

        for i in xrange(len(s)):
            if s[i] not in newdict:
                newdict[s[i]] = t[i]
            elif newdict[s[i]] != t[i]:
                return False
            else:
                pass
        return True

if __name__=="__main__":
    s = Solution()
    print s.isIsomorphic("add","egg")


