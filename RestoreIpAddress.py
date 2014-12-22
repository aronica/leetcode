__author__ = 'fafu'
class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        def __sub__(s,num,tmp,result):
            if len(s)<num or num == 0 or len(s)>3*num:
                return
            if num == 1:
                if len(s)>3:
                    return
                elif len(s)==3 and s.isdigit() and s[0]!='0' and s<"256":
                    tmp.append(s)
                    result.append(".".join(tmp))
                    return
                elif len(s)==2 and s.isdigit() and s[0]!='0':
                    tmp.append(s)
                    result.append(".".join(tmp))
                    return
                elif len(s)==1 and "0"<=s and s<"9":
                    tmp.append(s)
                    result.append(".".join(tmp))
                    return
            if len(s) == num:
                tmp.extend(s)
                for i in xrange(len(s)):
                    if s[i]>'9' and s[i]<'0':
                        return
                result.append(".".join(tmp))
                return
            length = len(tmp)
            if len(s) == num + 1:
                if "0"<=s[0] and s[0]<='9':
                    tmp.append(s[0])
                    __sub__(s[1:],num - 1,tmp,result)
                tmp = tmp[0:length]
                if s[0:2].isdigit() and s[0]!='0':
                    tmp.append(s[0:2])
                    __sub__(s[2:],num - 1,tmp,result)
            else:
                if "0"<=s[0] and s[0]<='9':
                    tmp.append(s[0])
                    __sub__(s[1:],num - 1,tmp,result)
                tmp = tmp[0:length]
                if s[0:2].isdigit() and s[0]!='0':
                    tmp.append(s[0:2])
                    __sub__(s[2:],num - 1,tmp,result)
                tmp = tmp[0:length]
                if s[0:3].isdigit() and s[0]!='0' and s[0:3] < "256":
                    tmp.append(s[0:3])
                    __sub__(s[3:],num - 1,tmp,result)

        if len(s) == 4:
            for i in s:
                if s<'0' or s>'9':
                    return []
            return [".".join(s)]
        if len(s) == 12:
            subarray = []
            for i in xrange(4):
                sub = s[i*3:(i+1)*3]
                if sub>"255" or not sub.isdigit() or s[0]=='0':
                    return []
                subarray.append(sub)
            return [".".join(subarray)]
        result = []
        __sub__(s,4,[],result)
        return result
if __name__=="__main__":
    s = Solution()
    print s.restoreIpAddresses("172162541")
