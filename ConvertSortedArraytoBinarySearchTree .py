#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'fafu'
from Meta import TreeNode


class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if num is None or len(num) == 0:
            return None
        if len(num) == 1:
            return TreeNode(num[0])
        root = TreeNode(num[(len(num) >> 1)])
        root.left = self.sortedArrayToBST(num[0:len(num) >> 1])
        root.right = self.sortedArrayToBST(num[(len(num) >> 1) + 1:])
        return root


if __name__ == '__main__':
    s = Solution()
    li = [1, 2, 3, 4, 5, 6]
    result = s.sortedArrayToBST(li)
    print li
    li = [1, 2]
    result = s.sortedArrayToBST(li)
    print li
    li = [1, 2, 3]
    result = s.sortedArrayToBST(li)
    print li
	