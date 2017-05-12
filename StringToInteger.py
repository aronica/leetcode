__author__ = 'fafu'
class Solution:


    #string to integer
    def atoi(self, str):
        if str is None:
            return 0

        str = str.strip()
        tmp = 0
        start = 0

        if len(str) == 0:
            return 0
        sign = 0
        if str[0] == "-":
            sign = 1
            start = 1
        elif str[0] == "+":
            sign = 0
            start = 1
        elif not self.isNumeric(str[0]):
            return
        else:
            #tmp = int(str[0])
            pass
        for j in range(start,len(str)):
            i = str[j]
            if not self.isNumeric(i):
                break
            if sign == 0:
                if tmp>214748364 or (tmp == 214748364 and int(i)>7):
                    return 2147483647
            elif sign == 1:
                if tmp>214748364 or (tmp == 214748364 and int(i)>8):
                    return -2147483648
            tmp = tmp*10 + int(i)
        if sign == 1:
            return tmp*-1
        return tmp

    def isNumeric(self,char):
        return "0"<=char and char<="9"
