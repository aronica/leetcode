__author__="fafu"
#TODO
from Meta import Interval

class Solution:
    def insert(self, intervals, newInterval):
        if intervals is None or len(intervals)==0:
            if newInterval is not None:
                return [newInterval]
            else:
                return []
        if newInterval.start>intervals[-1].end:
            intervals.append(newInterval)
            return intervals
        if newInterval.end<intervals[0].start:
            intervals.insert(0,newInterval)
            return intervals
        result = []
        map(lambda a:result.extend([a.start,a.end,'#']), intervals)
        i = 0
        val = newInterval.start
        start = True
        while i<len(result)-1:
            if result[i] == '#':
                if start:
                    i += 1
                else:
                    if i<len(A)-2:
                        if result[i+1]<=val:
                            del result[i]
                        else:
                            result.insert(i,val)
                    start = None
                    break
            elif result[i]<val:
                i += 1
            elif result[i]==val:
                if start == True:
                    start = False
                    val = newInterval.end
                    i += 1
                elif start == False:
                    start = None
                    break
            elif result[i]>val:
                result.insert(i,val)
                if start == True:
                    start = False
                    val = newInterval.end
                    i += 1
                elif start == False:
                    start = None
                    i += 1
                    result.insert(i,'#')
                    break
        if start == False:
            result[-1] = newInterval.end
        re = []
        i = 0
        st = True
        it = Interval()
        while i<=len(result)-1:
            if st and result[i]!='#':
                it.start = result[i]
                st = False
                i+=1
            elif not st and result[i]!='#' and i!=len(result)-1:
                i += 1
            elif not st and result[i] == '#' or i==len(result)-1:
                if result[i] == '#':
                    it.end = result[i-1]
                else:
                    it.end = result[i]
                i += 1
                re.append(it)
                it = Interval()
                st = True
        return re







        #This solution below occurs "Output Limit Exceeded"
        # result = []
        # it = False
        # for index,interval in enumerate(intervals):
        #     if interval.start<=newInterval.start and interval.end>=newInterval.end:
        #         return intervals
        #     if index != len(intervals)-1 and interval.end<newInterval.start and newInterval.end<intervals[index+1].start:
        #         intervals.insert(index+1,newInterval)
        #         return intervals
        #
        #     if not it:
        #         if interval.end<newInterval.start:
        #             result.append(interval)
        #             continue
        #         if interval.end == newInterval.start:
        #             interval.end = newInterval.end
        #             it = True
        #             result.append(interval)
        #             continue
        #         elif interval.end>newInterval.start:
        #             if interval.start>=newInterval.start:
        #                 interval.start = newInterval.start
        #                 it = True
        #                 result.append(interval)
        #                 continue
        #             elif interval.start<newInterval.start:
        #                 interval.end = max(interval.end,newInterval.end)
        #                 it = True
        #                 result.append(interval)
        #     else:
        #         if result[-1].end<interval.start:
        #             result.extend(intervals[index:])
        #             return result
        #         elif result[-1].end==interval.start:
        #             result[-1].end = interval.end
        #             result.extend(intervals[index:])
        #             return result
        #         else:
        #             #result[-1].end>interval.start
        #             if result[-1].end>=interval.end:
        #                 continue
        #             else:
        #                 result[-1].end = interval.end
        #                 result.extend(intervals[index+1:])
        #                 return result
        # return result
if __name__=="__main__":
    s = Solution()
    it1 = [Interval(1,5)]#,Interval(7,12)]#,Interval(2,3)],Interval(6,7),Interval(8,10),Interval(12,16)]
    it2 = Interval(2,3)
    result = s.insert(it1,it2)
    print result
                        
            
            
                
            
        