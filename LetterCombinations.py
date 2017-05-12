__author__ = 'fafu'
class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if len(digits)==0:
            return []
        dic = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        result = []
        def __dfs__(digits,index,tmp,result):
            lens = len(tmp)
            for i in dic[int(digits[index])-2]:
                tmp.append(i)
                if index == len(digits)-1:
                    result.append(tmp)
                else:
                    __dfs__(digits,index+1,tmp,result)
                tmp = tmp[0:lens]
        __dfs__(digits,0,[],result)
        return ["".join(i) for i in result]
if __name__=="__main__":
    s = Solution()
    print s.letterCombinations("23")






