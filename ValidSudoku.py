__author__ = 'fafu'


class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        def isValidArray(A):
            B=filter(lambda x:x!='.',A)
            S=set(B)
            return len(S)==len(B)
        def getline(A,num,row=True):
            if row:
                res=[A[num][i] for i in range(len(A[1]))]
            else:
                res=[A[i][num] for i in range(len(A))]
            return res
        def getsubboard(A,num):
            row=num/3*3
            col=num%3*3
            res=[A[i][j] for i in range(row,row+3) for j in range(col,col+3)]
            return res
        for i in range(len(board)):
            row=getline(board,i)
            col=getline(board,i,row=False)
            subboard=getsubboard(board,i)
            if not isValidArray(row) or  not isValidArray(col) or not isValidArray(subboard):
                return False
        return True




