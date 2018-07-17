class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) < 1:
            return None

        dp = [[0 for i in range(len(s))] for i in range(len(s))]
        maxlen = 1
        i = 0
        start = 0
        while i < len(s):
            j = 0
            while j <= i:
                if i - j < 2:
                    if s[i] == s[j]:
                        dp[j][i] = 1
                        if i - j + 1 > maxlen:
                            maxlen = i - j + 1
                            start = j
                else:
                    if s[i] == s[j] and dp[j + 1][i - 1] == 1:
                        dp[j][i] = 1
                        if i - j + 1 > maxlen:
                            maxlen = i - j + 1
                            start = j
                j += 1
            i += 1

        return s[start:(maxlen + start)]

if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("cbbd"))
    # print(s.longestPalindrome("PATZJUJZTACCBCC"))