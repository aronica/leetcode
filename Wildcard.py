__author__ = 'fafu'


class Solution:
    """
    '?' Matches any single character.
    '*' Matches any sequence of characters (including the empty sequence).

    The matching should cover the entire input string (not partial).

    The function prototype should be:
    bool isMatch(const char *s, const char *p)

    Some examples:
    isMatch("aa","a")  false
    isMatch("aa","aa") true
    isMatch("aaa","aa")  false
    isMatch("aa", "*")  true
    isMatch("aa", "a*")  true
    isMatch("ab", "?*") true
    isMatch("aab", "c*a*b")  false
    """
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        if p is None or len(p) == 0: return s is None or len(s) == 0
        if s is None or len(s) == 0: return p is None or len(p) == 0 or len(p) * "*" == p
        if p[0] == s[0] or p[0] == "?": return self.isMatch(s[1:], p[1:])
        newp = []
        for i in xrange(len(p)):
            if p[i] != "*":
                newp.append(p[i])
            else:
                if len(newp) == 0:
                    newp.append("*")
                    continue
                if newp[-1] != "*":
                    newp.append(p[i])
        p = newp
        if p[0] == "*":
            for i in xrange(len(s)-(len(p)-1-p[1:].count("*")), -1, -1):
                if self.isMatch(s[i:], p[1:]):
                    return True
        return False

import time
if __name__ == "__main__":
    s = Solution()
    print s.isMatch(
        "aaaabaaaabbbbaabbbaabbaababbabbaaaababaaabbbbbbaabbbabababbaaabaabaaaaaabbaabbbbaababbababaabbbaababbbba",
        "*****b*aba***babaa*bbaba***a*aaba*b*aa**a*b**ba***a*a*")
    print time.clock()
    print s.isMatch("abbaabbbbababaababababbabbbaaaabbbbaaabbbabaabbbbbabbbbabbabbaaabaaaabbbbbbaaabbabbbbababbbaaabbabbabb", "***b**a*a*b***b*a*b*bbb**baa*bba**b**bb***b*a*aab*a**")
    print time.clock()


