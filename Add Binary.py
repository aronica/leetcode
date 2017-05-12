__author__ = 'fafu'
class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        if a is None or len(a) == 0:
            return b
        if b is None or len(b) == 0:
            return a
        big = len(a)>len(b) and a or b
        small = len(a)>len(b) and b or a
        longs = len(big)
        short = len(small)
        result = ["0" for i in xrange(0,longs+1)]
        i = 0
        resultlength = longs + 1
        target = small
        while i<longs:
            if i == short:
                target = result
                short = resultlength
            if big[longs-i-1]>'9' or big[longs-i-1]<'0':
                return None
            if target==small and target[short-i-1]>'9' or target[short-i-1]<'0':
                return None
            if big[longs-i-1] == "0" and target[short - i -1] == "1" \
                or (big[longs-i-1] == "1" and target[short - i -1] == "0"):
                if target == result or result[resultlength-i-1]=="0":
                    result[resultlength-i-1] = "1"
                else:
                    result[resultlength-i-1] = "0"
                    result[resultlength-i-2] = "1"
            elif big[longs-i-1] == "1" and target[short - i -1] == "1":
                if target != result:
                    result[resultlength-i-2] = "1"
                else:
                    result[resultlength-i-2] = "1"
                    result[resultlength-i-1] = "0"
            i += 1
        if result[0] == "0":
            return "".join(result[1:])
        return "".join(result)
