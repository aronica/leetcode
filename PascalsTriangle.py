__author__ = 'fafu'
class Solution:
    #Pascal's Triangle
    def generate(self, numRows):
        if numRows is None or numRows == 0:
            return [[]]
        i = 1
        out = list()
        last = [1]
        out.append(last)
        while i < numRows:
            j = 1
            inner = list()
            inner.append(1)
            while j < i:
                inner.append(last[j - 1] + last[j])
                j += 1
            inner.append(1)
            last = inner
            out.append(inner)
            i += 1
        return out
