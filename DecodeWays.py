__author__ = 'fafu'
class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        def __decoding__(s,dic):
            if len(s) == 0:
                return 0
            if len(s)==1:
                return 1
            if s in dic:
                return dic[s]
            if s[0] > '2':
                num = self.numDecodings(s[1:])
                dic[s] = num
                return num
            if s[0] == '2':
                if s[1] == '0':
                    num = self.numDecodings(s[2:])
                    dic[s] = num
                    return num
                if s[1]<'7':
                    num1 = self.numDecodings(s[2:])
                    num2 = self.numDecodings(s[1:])
                    val = num1 + num2
                    dic[s] = val
                    return val
                else:
                    num1 = self.numDecodings(s[2:])
                    dic[s] = num1
                    return num1
            elif s[0] == '1':
                if s[1] == '0':
                    num = self.numDecodings(s[2:])
                    dic[s] = num
                    return num
                num1 = self.numDecodings(s[2:])
                num2 = self.numDecodings(s[1:])
                val = num1 + num2
                dic[s] = val
                return val
            else:
                num2 = self.numDecodings(s[1:])
                dic[s] = num2
                return num2
        dic = dict()
        return __decoding__(s,dic)
if __name__=="__main__":
    s = Solution()
    print s.numDecodings("1212312321313213213")











