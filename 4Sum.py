class Solution:
    def fourSum(self, num, target):
        if num is None or target is None or len(num)<4:
            return []
        num = sorted(num)
        dic = dict()
        for i in num:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        result = []
        for i in xrange(0, len(num) - 3):
            j = len(num) - 1
            dic[num[i]] -= 1
            while j > i + 2:
                dic[num[j]] -= 1
                m = i + 1
                while m < j - 1:
                    dic[num[m]] = dic[num[m]] - 1
                    left = target - num[m] - num[j] - num[i]
                    if left in dic and dic[left] > 0:
                        res = sorted([num[i], num[m], left, num[j]])
                        if len(result) > 0:
                            if result[-1][0] != res[0] or result[-1][1] != res[1] or result[-1][2] != res[2] or result[-1][
                                3] != res[3]:
                                result.append(tuple(res))
                        else:
                            result.append(tuple(res))
                    dic[num[m]] += 1
                    m += 1
                dic[num[j]] += 1
                j -= 1
        return result


s = Solution()
print s.fourSum([-489,-475,-469,-468,-467,-462,-456,-443,-439,-425,-425,-410,-401,-342,-341,-331,-323,-307,-299,-262,-254,-245,-244,-238,-229,-227,-225,-224,-221,-197,-173,-171,-160,-142,-142,-136,-134,-125,-114,-100,-86,-81,-66,-47,-37,-34,4,7,11,34,60,76,99,104,113,117,124,139,141,143,144,146,157,157,178,183,185,189,192,194,221,223,226,232,247,249,274,281,284,293,298,319,327,338,340,368,375,377,379,388,390,392,446,469,480,490], 2738)