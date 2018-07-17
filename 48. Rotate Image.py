"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

A:解题思路，先按照水平方向交换（第一行和最后一行交换，第二行和倒数第二行交换），然后按照对角线交换（matrix[i][j] <=> matrix[j][i]）。
"""


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if matrix is None or len(matrix) < 2:
            return
        n = len(matrix)
        for i in xrange(n / 2):
            for j in xrange(n):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n - i - 1][j]
                matrix[n - i - 1][j] = tmp
        for i in xrange(n - 1):
            j = i + 1
            while j < n:
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
                j += 1



if __name__ == "__main__":
    a = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    s = Solution()
    s.rotate(a)
    print a