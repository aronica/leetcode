__author__ = 'fafu'
class Solution:
    #Is Number
    def isNumber(self, s):
        if s is None:
            return False
        s = s.strip()
        if len(s) == 0:
            return False
        if s[0] == "e" or s[0] == "E" or s[len(s)-1] == "e" or s[len(s) -1] == "E":
            return False

        ecount = -1
        pointcount = -1
        pointhead = False
        sign = -1
        for index,i in enumerate(s):
            if i.isdigit():
                continue
            elif i == "e" or i == "E":
                if pointhead and index == 1:
                    return False
                if ecount == -1:
                    if i == (len(s) - 1) or i == 0:
                        return False
                    ecount = index
                else:
                    return False
            elif i == "." :
                if sign == 0 and index == 1 and len(s) == 2:
                    return False
                if ecount != -1:
                    return False

                if index == 0:
                    pointhead = True
                if pointcount == -1:
                    if len(s) == 1:
                        return False
                    pointcount = index
                else:
                    return False
            elif i=="-" or i== "+":
                if index == 0:
                    sign = 0
                elif ecount != (index-1):
                    return False
                elif index == len(s)-1:
                    return False

            else:
                return False
        return True