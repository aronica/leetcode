__author__ = 'fafu'
class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        def __cmp1__(this,other):
            if this<other:
                return 1
            elif this ==other:
                return 0
            else:return -1
        def __cmps__(this,other):
            s1 = len(this)
            s2 = len(other)
            long,short=None,None
            if s1<s2:
                short = this
                long = other
            else:
                short =other
                long = this
            if long[0:len(short)]!=short:
                return __cmp1__(this,other)
            else:
                s1 = this+other
                s2 = other + this
                if s1>s2:
                    return -1
                elif s1==s2:
                    return 0
                else:
                    return 1


        if num is None or len(num) == 0:return None
        s = map(lambda a:str(a),num)
        s.sort(cmp=__cmps__)
        res =  "".join(s)
        res = res.lstrip('0')
        if len(res)==0:return "0"
        return res
if __name__=="__main__":
   s = Solution()
   print s.largestNumber([121,12,0])
   print s.largestNumber([0,0])
