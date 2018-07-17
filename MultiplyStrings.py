__author__ = 'fafu'


class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        if len(num1) == 0 or len(num2) == 0 :
            return "0"
        large, small = num1, num2
        if num1 < num2:
            large = num2
            small = num1
        m = len(large)
        total = [0 for i in xrange(len(num1) + len(num2))]
        a = [0 for x in xrange(m + 1)]
        for i in xrange(len(small) - 1, -1, -1):
            self.__clear__(a)
            for j in xrange(m - 1, -1, - 1):
                tmp = int(small[i]) * int(large[j])
                Solution.add_array_value(a, j + 1, tmp)
            Solution.add_two_array(total, m + i, a)
        start = 0
        while start < len(total) - 1:
            if total[start] != 0:
                break
            start += 1
        return "".join([str(i) for i in total[start:]])

    @staticmethod
    def __clear__(arr):
        for i in xrange(len(arr)):
            arr[i] = 0

    @staticmethod
    def add_two_array(arr1, arr1_index, arr2):
        arr1_current_index = arr1_index
        for i in xrange(len(arr2) - 1, -1, -1):
            arr1[arr1_current_index] += arr2[i]
            arr1_current_index -= 1
        for i in xrange(arr1_index, 0, -1):
            if arr1[i] >= 10:
                inc = arr1[i] / 10
                arr1[i] = arr1[i] % 10
                arr1[i - 1] += inc

    @staticmethod
    def add_array_value(arr1, start_index, value):
        index = start_index
        tmp = str(value)
        for a in xrange(len(tmp) - 1, -1, -1):
            arr1[index] += int(tmp[a])
            index -= 1
        for a in xrange(start_index, 0, -1):
            if arr1[a] >= 10:
                inc = arr1[a] / 10
                arr1[a] = arr1[a] % 10
                arr1[a - 1] += inc


if __name__ == '__main__':
    s = Solution()
    a = "0"
    b = "0"
    print int(a)*int(b)
    print s.multiply(a,b)
    # a = "9369162965141127216164882458728854782080715827760307787224298083754"
    # b = "7204554941577564438"
    # s = Solution()
    # print int(a) * int(b)
    # print s.multiply(a, b)
    # a = "0"
    # b = "0"
    # print s.multiply(a, b)
