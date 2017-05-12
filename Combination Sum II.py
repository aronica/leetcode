__author__ = 'fafu'
class Solution:
    #combination sum2: each element in candidates may only be used once.
    def combinationSum2(self, candidates, target):
        def __combines__(candidates,dic,target):
            i = len(candidates)-1
            result = []
            while i>-1:
                if i != 0 and candidates[i] == candidates[i-1]:
                    i -= 1
                    continue
                if target<candidates[i]:
                    i -= 1
                    continue
                val = dic[candidates[i]]
                for j in xrange(val,0,-1):
                    tmp = target - j*candidates[i]
                    if tmp == 0:
                        result.append([candidates[i] for m in xrange(j)])
                        continue
                    elif tmp<candidates[0]:
                        continue
                    res = __combines__(candidates[0:i],dic,tmp)
                    for m in res:
                        m.extend([candidates[i] for n in xrange(j)])
                    result.extend(res)
                i -= 1
            return result

        candidates.sort()

        while len(candidates)>0 and candidates[len(candidates)-1]>target:
            candidates.pop()

        if len(candidates)==1:
            if candidates[0] == target:
                return [[target]]
            else:
                return []
        dic={}
        for i in candidates:
            if i in dic:
                dic[i] = dic[i]+1
            else:
                dic[i] = 1
        i = 0;j=len(candidates)-1
        result = []
        return __combines__(candidates,dic,target)

