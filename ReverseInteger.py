__author__ = 'fafu'
class Solution:
    # @return an integer
    map = {str(i):i for i in xrange(10)}
    def reverse(self, x):
        if -10<x and x<10:
            return x
        negative = False
        if x < 0:
            negative = True
            x = -x
        s = str(x)
        #current = 0
        i = len(s)-1
        while s[i] == '0':
            i -= 1
        if i == 0:
            if negative:
                return -int(s[0])
            else:
                return int(s[0])
        if int(s[-1])>2 and len(s)>=10:
            return 0
        length = i+1
        current = int(s[i])
        i -= 1
        maxes = [2,1,4,7,4,8,3,6,4,8]
        maxes2 = 2147483647
        while i>=0:
            val = int(s[i])
            if length<10:
                current = current*10 + val
            else:
                if current>maxes2/pow(10,i + 1):
                    return 0
                elif current == maxes2/pow(10,i + 1):
                    if val > maxes[length-i-1]:
                        return 0
                    elif val == maxes[length-i-1]:
                        if i == 0 and val == 8 and not negative:
                            return 0
                        else:
                            current = current*10 + val
                    else:
                        current = current*10 + val
                else:
                    current = current*10 + val
            i -= 1
        if negative:
            return -current
        return current
if __name__=="__main__":
    s = Solution()
    a = 100
    print a,s.reverse(a)
    a = -1003
    print a,s.reverse(a)
    a = 1000000003
    print a,s.reverse(a)
    a = 7463847412
    print a,s.reverse(a)
    a = 1463947412
    print a,s.reverse(a)
    a = -1563847412
    print a,s.reverse(a)





