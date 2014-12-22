__author__ = 'fafu'
class Solution:

    #Pascal's Triangle II
    def getRow(self, rowIndex):
        if rowIndex is None or rowIndex < 0:
            return []
        result = list()
        i = 1
        result.append(1)
        while i < rowIndex + 1:
            j = i - 1
            result.append(1)
            while j > 0:
                result[j] = result[j - 1] + result[j]
                j -= 1
            i += 1
        return result
