import time

__author__ = 'fafu'

QM = "?"
STAR = "*"


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
        if p is None or len(p) == 0:
            return s is None or len(s) == 0
        if s is None or len(s) == 0:
            return p is None or len(p) == 0 or p.count("*") == p
        m, n = len(s), len(p)
        indexP, indexS = 0, 0
        indexP_start = -1
        indexS_match = 0
        while indexS < m:
            if indexP < n and (s[indexS] == p[indexP] or p[indexP] == QM):
                indexP += 1
                indexS += 1
            elif indexP<n and p[indexP] == STAR:
                indexP_start = indexP
                indexP += 1
                indexS_match = indexS
            elif indexP_start != -1:
                indexP = indexP_start + 1
                indexS_match += 1
                indexS = indexS_match
            else:
                return False

        while indexP < n:
            if p[indexP] != STAR:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    # print s.isMatch("aa", "a") == False
    # print s.isMatch("aa", "??") == True
    print s.isMatch("adceb", "*a*b") == True

    print s.isMatch("aadd", "aaddf") == False
    print s.isMatch("aaddff", "aaddf") == False
    print s.isMatch("aaaaadd", "????") == False

    print s.isMatch("adceb", "*a*b") == True

    print s.isMatch("aa", "*??") == True
    print s.isMatch("aa", "aa") == True
    print s.isMatch("aaa", "aa") == False
    print s.isMatch("aa", "*") == True
    print s.isMatch("aa", "a*") == True
    print s.isMatch("ab", "?*") == True
    print s.isMatch("aab", "c*a*b") == False
    ss = "aaaabaaaabbbbaabbbaabbaababbabbaaaababaaabbbbbbaabbbabababbaaabaabaaaaaabbaabbbbaababbababaabbbaababbbba"
    pp = "*b*aba*babaa*bbaba*a*aaba*b*aa**a*b**ba*a*a"
    print s.isMatch(ss, pp) == True
    print time.clock()
    ss = "abbaabbbbababaababababbabbbaaaabbbbaaabbbabaabbbbbabbbbabbabbaaabaaaabbbbbbaaabbabbbbababbbaaabbabbabb"
    pp = "*b*a*a*b*b*a*b*bbb*baa*bba*b*bb*b*a*aab*a*"
    print s.isMatch(ss, pp) == True
    print time.clock()
