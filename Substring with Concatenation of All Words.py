class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        if S is None or L is None or len(L) == 0 or len(L[0]) == 0 or len(S) < len(L[0]) * len(L):
            return []
        result = []
        resultset = set()
        target = dict({i:0 for i in L})
        for t in L:target[t] += 1
        lens = len(L[0])
        i = 0
        while i + len(L[0]) * len(L) <= len(S):
            if i - lens in resultset and S[i - lens:i] == S[i - lens + len(L[0]) * len(L):i + len(L[0]) * len(L)]:
                result.append(i)
                resultset.add(i)
                i += 1
                continue
            target_clone = dict(target)
            j = i
            found = 0
            startindex = j
            while j + lens < len(S) + 1 and S[j:j + lens] in target_clone and target_clone[S[j:j + lens]] > 0:
                target_clone[S[j:j + lens]] -= 1
                found += 1
                if found == len(L):
                    result.append(startindex)
                    resultset.add(startindex)
                    break
                j += lens
            i += 1
        return result


if __name__ == "__main__":
    s = Solution()
    print s.findSubstring("barfoothefoobarman", ["foo", "bar"])
    print s.findSubstring("aaa",["a","a"])
    print s.findSubstring("abbaccaaabcabbbccbabbccabbacabcacbbaabbbbbaaabac"+""
    "caacbccabcbababbbabccabacbbcabbaacaccccbaabcabaabaaaabcaabcacabaa" ,
                          ["cac","aaa","aba","aab","abc"])








