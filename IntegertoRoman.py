__author__ = 'fafu'
from RomantoInteger import Solution as RomanToInteger
class Solution:
    # @return a string
    def intToRoman(self, num):
        items = [("I",1),("V",5),("X",10),("L",50),("C",100),("D",500),("M",1000)]
        result = ""
        left = num
        i = len(items)-1
        while i>-1:
            pro = left/items[i][1]
            if pro>0 and pro<4:
                result += (pro)*items[i][0]
                left = num%items[i][1]
                i -= 2
            elif pro == 4:
                result += items[i][0]+items[i+1][0]
                left -= items[i+1][1]-items[i][1]
                i -= 2
            elif pro>4 and pro<9:
                result += items[i+1][0]
                left -= items[i+1][1]

            elif pro==9:
                result += items[i][0]+items[i+2][0]
                left -= items[i+2][1] - items[i][1]
                i -= 2
            else:
                i -= 2
            if left == 0:
                break
        return result
if __name__=="__main__":
    s = Solution()
    i = 1
    print 6,s.intToRoman(6)
    print 91,s.intToRoman(91)
    rt = RomanToInteger()
    while i<4000:
        if rt.romanToInt(s.intToRoman(i))!=i:
            print "Error:",i,s.intToRoman(i)
            break
        else:
            print i,s.intToRoman(i),"is ok"
        i += 1
    print "ok"








