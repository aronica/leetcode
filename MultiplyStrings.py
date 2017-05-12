__author__ = 'fafu'
class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        m = len(num1)
        n = len(num2)
        if m == 0:
            return num2
        if n == 0:
            return num1
        if m+n<8:
            return str(int(num1)*int(num2))
        i ,j = 0,0
        result = []
        while m-i*4>0:
            j = 0
            while n-j*4>0:
                s1 = num1[max(0,m-(i+1)*4):m-i*4]
                s2 = num2[max(0,n-(j+1)*4):n-j*4]
                res = str(int(s1)*int(s2))
                zeros = 4*i+4*j
                res += "0"*zeros
                result.append(res)
                j += 1
            i += 1
        i,j = 0,0
        res = None
        while True:
            tmp = 0
            found = False
            for j in xrange(len(result)):
                if len(result[j]) - (i+1)*5 - 1>=0:
                    tmp += int(result[j][max(0,len(result[j]) - (i+1)*5 - 1):len(result[j]) - i*5 - 1])
                    found = True
            if not found:
                return "".join(res)
            if res is None:
                res = list(str(tmp))
            else:
                if len(res)-1-i*5<0:
                    tmp = str(tmp)
                    for m in xrange(len(tmp)-1,-1,-1):
                        res.insert(0,tmp[m])
                else:
                    val = str(int("".join(res[0:len(res)-i*5])) + tmp)
                    res = list(val)+res[len(res)-i*5:]
            i += 1
        return "".join(res)
if __name__=='__main__':
    a = "9369162965141127216164882458728854782080715827760307787224298083754"
    b = "7204554941577564438"
    s = Solution()
    print int(a)*int(b)
    print s.multiply(a,b)
    a ="0"
    b = "0"
    print s.multiply(a,b)
















