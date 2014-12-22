__author__ = 'fafu'
class Solution:
    #divide two integers
    def divide(self, dividend, divisor):
        if dividend is None or divisor is None:
            return None
        if divisor == 0:
            return None
        if dividend == 0:
            return 0


        pos = True
        if dividend <0 and divisor<0:
            dividend = 0 -  dividend
            divisor = 0 - divisor

        if (dividend>0 and divisor <0) or (dividend<0 and divisor>0):
            pos = False

        if not pos:
            if dividend < 0:
                dividend = 0 - dividend
            elif divisor < 0:
                divisor = 0 - divisor
        if pos:
            if dividend< divisor:
                return 0
        else:
            if dividend<divisor:
                return 0


        partial = []
        cumulative = divisor
        times = 1
        while dividend >= cumulative:
            partial.append((cumulative,times))
            cumulative = cumulative<<1
            time = times<<1

        pair = partial.pop()
        result = pair[1]
        dividend -= pair[0]

        index = len(partial)
        while dividend >= divisor and len(partial)>0:
            pair = partial.pop()
            value = pair[0]
            times = pair[1]
            if dividend >= value:
                result += times
                dividend -= value
        if pos:
            return result
        else:
            if dividend == 0:
                return -result
            else:
                return -result

