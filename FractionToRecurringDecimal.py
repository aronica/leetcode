__author__ = 'fafu'
class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        if numerator is None or denominator is None:
            return None
        negative = False
        if numerator<0 and denominator>0 or (numerator>0 and denominator<0):
            negative = True
        numerator = abs(numerator)
        denominator = abs(denominator)
        intergerpart = numerator/denominator
        fractionpart = numerator%denominator
        fraction = fractionpart
        result = str(intergerpart)
        if fractionpart == 0:
            if negative:
                return -result
            return result
        result += "."
        dis = dict()
        while True:
            zero = 0
            fraction *= 10
            resultlen = len(result)+1
            while fraction<denominator:
                dis[fraction] = resultlen
                fraction *= 10
                zero += 1
                resultlen += 1
            newintegerpart = fraction/denominator
            newfractionpart = fraction%denominator
            if newfractionpart == 0:
                result = result + "0"*zero + str(newintegerpart)
                break
            else:
                if newfractionpart in dis:
                    length = dis[newfractionpart]
                    if result[length:]!="0"*zero+str(newintegerpart):
                        result = result + "0"*zero + str(newintegerpart)
                    lens = len(result[length:])
                    if result[0:-lens-1]== "0"*zero + str(newintegerpart):
                        result = result[0:len(result)-len()] + "(" + "0"*zero + str(newintegerpart)+")"
                    else:
                        result = result[0:length] + "(" + result[length:]+")"
                    break
                else:
                    dis[fractionpart] = len(result)
                    result += "0"*zero + str(newintegerpart)
                    fractionpart = newfractionpart
                    fraction = fractionpart

        left = result.find("(")
        if left !=-1:
            right = result.rindex(")")
            repeat = result[left+1:right]
            lens = right - left -1
            if result[left-lens:left]==result[left+1:right]:
                result = result[0:left-lens] +"("+repeat+")"
        if negative:
            return "-"+result
        return result
if __name__=="__main__":
    s = Solution()
    # print "2/3",s.fractionToDecimal(2,3)
    # print "2/1",s.fractionToDecimal(2,1)
    # print "3/2",s.fractionToDecimal(3,2)
    # print "1/81",s.fractionToDecimal(1,81)
    # print "1/214748364",s.fractionToDecimal(1,214748364)
    print "-2147483648/1",s.fractionToDecimal(-2147483648,1)




