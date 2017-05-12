__author__ = 'fafu'


class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0: return []
        result = []
        m,n = len(matrix),len(matrix[0])
        top, right, bottom, left = -1, len(matrix[0]), len(matrix), -1
        i,j = 0,0
        while left<right-1 or top<bottom-1:
            if left<right-1:
                i = left + 1
                j = top + 1
                while j<right:
                    result.append(matrix[i][j])
                    j += 1
                top = i
                j -= 1
            else:
                break
            if top<bottom-1:
                i = top + 1
                while i<bottom:
                    result.append(matrix[i][j])
                    i += 1
                right = j
                i -= 1
            else:
                break
            if left<right-1:
                j = right -1
                while j>left:
                    result.append(matrix[i][j])
                    j -= 1
                bottom = i
                j += 1
            else:
                break
            if top<bottom-1:
                i = bottom -1
                while i>top:
                    result.append(matrix[i][j])
                    i -= 1
                left = j
                i += 1
            else:
                break
        return result

if __name__=="__main__":
    s = Solution()
    print s.spiralOrder([
        [ 1, 2, 3,13,14 ],
        [ 4, 5, 6,15,16 ],
        [ 7, 8, 9,17,18 ],
        [10,11,12,19,20]
    ])

