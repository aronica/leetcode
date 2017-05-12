__author__ = 'fafu'
class Solution:
    #Find minimal in rotated sorted array
    def findMin(self, num):
        if num is None:
            return None
        return self.find(num, 0, len(num) - 1)

    def find(self, num, start, end):
        if end - start == 0:
            return num[start]
        if end - start == 1:
            return min(num[start], num[end])
        mid = start + (end - start) / 2
        if num[start] < num[mid] and num[mid] > num[end]:
            return self.find(num, mid + 1, end)
        elif num[start] < num[mid] and num[mid] < num[end]:
            return num[start]
        else:
            return self.find(num, start, mid)
