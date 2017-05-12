__author__ = 'fafu'

class Solution:
    #max product
    def maxProduct(self,A):
        if A is None or len(A) == 0:
            return 0
        if len(A) == 1:
            return A[0]
        maxone = A[0]
        # for i in A:
        #     if i>maxone:
        #         maxone = i
        amax = dict()
        if A[0] > 0:
            amax[0] = (None,None,A[0])
        elif A[0] < 0:
            amax[0] = (A[0],None,None)
        else:
            amax[0] = (None,0,None)

        for i in xrange(1,len(A)):
            #for j in xrange(0,i + 1):
            negmax = amax[i-1][0]
            zeromax = amax[i-1][1]
            posmax = amax[i-1][2]

            new_negmax = None
            new_zeromax = None
            new_posmax = None

            if A[i]<0:
                if negmax is not None:
                    new_posmax = negmax * A[i]
                if posmax is not None:
                    new_negmax = min(A[i],A[i]*posmax)
                else:
                    new_negmax = A[i]
                if zeromax is not None:
                    new_zeromax = 0
            elif A[i] == 0:
                new_posmax = 0
                new_negmax = 0
                new_zeromax = 0
            elif A[i]>0:
                if negmax is not None:
                    new_negmax = negmax*A[i]
                if posmax is not None:
                    new_posmax = max(A[i],A[i]*posmax)
                else:
                    new_posmax = A[i]
                if zeromax is not None:
                    new_zeromax = 0
            maxone = max(maxone,new_posmax,new_zeromax,new_negmax)
            amax[i] = (new_negmax,new_zeromax,new_posmax)
        return maxone

    #max product
    def maxProduct2(self, A):
        if A is None or len(A) == 0:
            return 0
        if len(A) == 1:
            return A[0]

        negative = 0
        maxone = A[0]
        for i in A:
            if i<0:
                negative += 1
            if i>maxone:
                maxone = i
        fn = 0
        if max < 0:
            fn = 1
        foundmax = max
        j = 1
        startindex = 0
        negativestart = -1
        if A[0] < 0:
            negativestart = 0
        while j<len(A):
            i = A[j]
            if abs(max) < 1:
                startindex = j
                max = i
                if i < 0:
                    if negativestart == -1:
                        negativestart = j
                else:
                    negativestart = -1
            else:
                if max < 0 and (negative - fn == 0):
                    max = i
                    startindex = j
                    if i < 0:
                        if negativestart == -1:
                            negativestart = j
                        else:
                            negativestart = -1
                    else:
                        negativestart = -1
                    j += 1
                    continue
                elif max < 0 and i<0:
                    max *=i
                    if negativestart == -1:
                        negativestart = j
                elif max > 0 and i<0 and negative-fn == 1:
                    if j < len(A)- 1:
                        if negativestart == -1:
                            max = A[j+1]
                            startindex = j + 1
                            if max < 0 and negativestart == -1:
                                negativestart = j + 1
                            else:
                                negativestart = -1
                            j = j + 2
                            continue
                        else:
                            currentmax = max
                            while startindex <= negativestart:
                                max /= A[startindex]
                                startindex += 1
                            found = False
                            max *= A[j]
                            newstart = startindex
                    else:
                        currentmax = max
                        max *= A[j]
                        if negativestart != -1:
                            while startindex<j:
                                max /= A[startindex]

                                if max>currentmax:
                                    currentmax = max
                                startindex+=1

                            max = currentmax
                        break
                else:
                    if i<0:
                        if negativestart == -1:
                            negativestart = j
                    max *= i
            if i<0:
                fn += 1
            if foundmax<max:
                foundmax = max
            if foundmax < i:
                foundmax = i
            j += 1
        if foundmax<max:
            foundmax = max
        if foundmax < maxone:
            foundmax = maxone
        return foundmax
