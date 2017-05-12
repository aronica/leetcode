__author__ = 'fafu'
class Solution:

    def isPalindrome(self, s):
        if s is None or len(s.strip()) == 0:
            return True
        s = s.strip()
        i = 0
        j = len(s) - 1
        while i < j:
            if not s[i:i + 1].isalnum():
                i += 1
                continue
            if not s[j:j + 1].isalnum():
                j -= 1
                continue
            first = s[i:i + 1]
            second = s[j:j + 1]
            if first.lower() != second.lower():
                return False
            i += 1
            j -= 1
        return True
