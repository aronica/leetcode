class Solution:
    def subsets(self,S):
        if S is None:
            return []
        if len(S) == 1:
            return [S,[]]
        S = sorted(S)    
        result = [[]]
        tmp = [[]]
        for i in S:
            if not (len(result)==1 and len(result[0])==0):
                tmp = [list(m) for m in result]
            for j in result:
                j.append(i)
            result.extend(tmp)
if __name__=="__main__":
    s = Solution()
    se1 = [1,2,2]
    print se1,s.subsets(se1)
    se2 = [2,3,4,1]
    print se2,s.subsets(se2)