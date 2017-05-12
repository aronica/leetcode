__author__ = 'fafu'
import time


class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        if p is None:
            return s is None
        if len(p) == 0:
            return len(s) == 0
        if len(p) == 1:
            return len(s) == 1 and (s[0] == p[0] or p[0] == ".")
        if p[1] != "*":
            return s is not None and len(s) >= 1 and (s[0] == p[0] or p[0] == ".") and self.isMatch(s[1:], p[1:])
        #remove redundant sub pattern as this :a*a*a*
        i = 0
        while (i + 3) < len(p) and p[i:i + 2] == p[i + 2:i + 4]:
            p = p[i + 2:]
            i += 2

        i = 0
        # p[1]=="*"

        while i < len(s) and (s[i] == p[0] or p[0] == "."):
            if self.isMatch(s[i:], p[2:]): return True
            i += 1
        return self.isMatch(s[i:], p[2:])


if __name__ == "__main__":
    s = Solution()
    assert s.isMatch("aa", "a") is False
    assert s.isMatch("aa", "aa") is True
    assert s.isMatch("aaa", "aa") is False
    assert s.isMatch("aa", "a*") is True
    assert s.isMatch("aa", ".*") is True
    assert s.isMatch("ab", ".*") is True
    print time.clock()
    assert s.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c") is False
    print time.clock()
    print s.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*a*a*b")



