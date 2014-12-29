__author__ = 'fafu'
class Solution:
    # @return an integer
    def romanToInt(self, s):
        if s is None or len(s)==0:
            return None
        dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        total = dic[s[0]]
        for i in xrange(1,len(s)):
            if dic[s[i]]<=dic[s[i-1]]:
                total += dic[s[i]]
            else:
                total -= dic[s[i-1]]*2
                total += dic[s[i]]
        return total
if __name__=="__main__":
    s = Solution()
    print "DCCC",s.romanToInt("DCCC")
    print "XXI",s.romanToInt("XXI")
    print "CMXCIX",s.romanToInt("CMXCIX")
    print "XXXIV",s.romanToInt("XXXIV")
    print "MMMCMXCIX",s.romanToInt("MMMCMXCIX")



