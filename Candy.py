class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        if ratings == None or len(ratings)==0:
            return 0
        if len(ratings)==1:
            return 1
        if len(ratings)==2:
            if ratings[0]==ratings[1]:
                return 2
            return 3
        sums = 1
        pre = 1
        index = 1
        result = [1]
        unfit = []

        while index<len(ratings):
            if ratings[index]>ratings[index-1]:
                if pre>=1:
                    pre += 1
                else:
                    pre = 2
            elif ratings[index]<ratings[index-1]:
                if pre>1:
                    pre = 1
                else:
                    pre -= 1
            else:
                pre = 1
            sums += pre
            result.append(pre)
            if pre<1:
                if len(unfit)== 0 or unfit[-1]!= index - 1:
                    unfit.append(index)
                else:
                    unfit[-1] = index
            index += 1
        i = len(unfit)-1
        while i>=0:
            if result[unfit[i]]<1:
                sums += 1 - result[unfit[i]]
                result[unfit[i]] = 1
                j = unfit[i] - 1
                l = unfit[i]
                while j>=0:
                    if ratings[j]> ratings[l] and result[j]<=result[l]:
                        sums += result[l]+1-result[j]
                        result[j] = result[l]+1
                    # elif ratings[j] == ratings[l] and result[j]<result[l]:
                    #     sums += result[l]-result[j]
                    #     result[j] = result[l]
                    else:
                        break
                    j -= 1
                    l -= 1
                if j == 0:
                    return sums
                else:
                    i -= 1
            else:
                i -= 1
        return sums
if __name__=="__main__":
    s = Solution()
    a = [4,2,3,4,1]
    print a
    res = s.candy(a)
    print res
    a =  [6 ,4 ,4  ,2  ,2  ,2 ,7  ,4  ,3  ,5  ,1  ,0  ,3]
    print a
    res = s.candy(a)
    print res





