__author__ = 'fafu'
class Solution:
    # @return a string
    def countAndSay(self, n):
        if n == 1:
            return "1"
        i = 1
        last = "1"
        while i<n:
            lens = len(last)
            j = 1
            result = []
            cumulative = 1
            ele = last[0]
            while j<lens:
                if last[j]==ele:
                    cumulative += 1
                else:
                    result.append(str(cumulative)+ele)
                    cumulative = 1
                    ele = last[j]
                j += 1
            result.append(str(cumulative)+ele)
            last = "".join(result)
            i += 1
        return last
if __name__=="__main__":
    s = Solution()
    print s.countAndSay(4)
    print s.countAndSay(5)
    print s.countAndSay(6)
    print s.countAndSay(7)



