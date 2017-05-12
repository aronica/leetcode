# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
from Meta import Interval
class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        if intervals is None or len(intervals)<2:
            return intervals
        intervals = sorted(intervals,cmp=lambda a,b:cmp(a.start,b.start))
        result = []
        last = intervals[0]
        for i in xrange(1,len(intervals)):
            if last.end<intervals[i].start:
                result.append(last)
                if i == len(intervals)-1:
                    result.append(intervals[-1])
                    return result
                last = intervals[i]
                continue
            elif last.end == intervals[i].start:
                last.end = intervals[i].end
            else:#last.end>intervals[i].start
                if intervals[i].end<=last.end:
                    pass
                else:#intervals[i].end>last.end
                    last.end = intervals[i].end
            if i == len(intervals)-1:
                result.append(last)
        return result
if __name__=="__main__":
    s = Solution()
    it = Interval(1,4)
    it2 = Interval(0,4)
    print s.merge([it,it2])
    
                    
                    
        
        