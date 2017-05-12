__author__ = 'fafu'
class Solution:
    #3Sum
    def threeSum(self, num):
        A = sorted(num)
        result = []
        i = 0
        pre = None
        while i<len(num)-2 and A[i] <= 0:
            if A[i] == pre:
                i += 1
                continue
            m = i+1
            n = len(num) -1
            while m<n:
                if A[m] + A[n] + A[i] == 0:
                    if len(result) >0:
                        tmp = result[len(result)-1]
                        if tmp[0] != A[i] or tmp[1] != A[m] or tmp[2] != A[n]:
                            result.append([A[i],A[m],A[n]])
                    else:
                        result.append([A[i],A[m],A[n]])
                    m += 1
                    n -= 1
                elif A[m] + A[n] > -A[i]:
                    n -= 1
                elif A[m] + A[n] < -A[i]:
                    m += 1
            pre = A[i]
            i += 1
        return result
