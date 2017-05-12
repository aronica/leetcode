__author__ = 'fafu'
class Solution:
    # @param a, a string
    # @param b, a string
    # @return a boolean
    def compareVersion(self, version1, version2):
        v1 = version1.split(".")
        v2 = version2.split(".")
        i = 0
        while i<len(v1) and i<len(v2):
            if int(v1[i])>int(v2[i]):
                return 1
            if int(v1[i])<int(v2[i]):
                return -1
            i += 1
        if i == len(v1) and i<len(v2):
            return -2
        if i == len(v2) and i<len(v1):
            return -1
        return 0

