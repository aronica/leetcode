__author__ = 'fafu'
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        def __combination__(candidates,target):
            sets = set(candidates)
            result = []
            for i in xrange(len(candidates)-1,-1,-1):
                val = target/candidates[i]
                remainder = target%candidates[i]
                if remainder == 0:
                    result.append([candidates[i] for j in xrange(val)])

                for j in xrange(val,0,-1):
                    tmp = target - j*candidates[i]
                    if tmp == 0:
                        continue
                    elif tmp<candidates[0]:
                        continue
                    res = __combination__(candidates[0:i],tmp)
                    for m in res:
                        m.extend([candidates[i] for n in xrange(j)])
                    result.extend(res)
            return result

        if candidates is None or len(candidates)==0:
            return []
        if target is None or target<1:
            return None

        while len(candidates)>0 and candidates[len(candidates)-1]>target:
            candidates.pop()
        candidates.sort()
        return __combination__(candidates,target)

