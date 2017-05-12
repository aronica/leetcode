__author__ = 'fafu'

class Cell:
    def __init__(self,type,index,empty,missing,total):
        self.type = type
        self.index = index
        self.empty = empty
        self.missing = missing
        self.total = total
    def __lt__(self, other):
        return len(self.missing)<len(other.missing)

class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        def getqueue(board):
            queue = []
            for i in range(len(board)):
                row = getline(board, i)
                col = getline(board, i, row=False)
                subboard = getsubboard(board, i)
                queue.append(row)
                queue.append(col)
                queue.append(subboard)
            return queue

        def isValidArray(A):
            B=filter(lambda x:x!='.',A.total)
            S=set(B)
            return len(S)==len(B)

        def getline(A,num,row=True):
            if row:
                res=[A[num][i] for i in range(len(A[1]))]
                return Cell("row",num,[(num,i) for i in range(len(A[1])) if A[num][i]=="."],set([i for i in xrange(1,10)])-set(res),res)
            else:
                res=[A[i][num] for i in range(len(A[1]))]
                return Cell("column",num,[(i,num) for i in range(len(A[1])) if A[i][num]=="."],set([i for i in xrange(1,10)])-set(res),res)

        def getsubboard(A,num):
            row=num/3*3
            col=num%3*3
            res=[A[i][j] for i in range(row,row+3) for j in range(col,col+3)]
            return Cell("subboard",num,[(i,j) for i in range(row,row+3) for j in range(col,col+3) if A[i][j]=="."],
                        set([i for i in xrange(1,10)])-set(res),res)

        def getboardindex(i,j):
            return j/3 + (i/3)*3



        def calculate(board,result):
            queue = getqueue(board)
            top = min(queue,key=lambda x:len(x.missing))
            empty = top.empty
            missing = top.missing
            if len(queue[-1].missing)==0:
                result.append(board)
                return True
            originboard = list(board)
            for i in empty:
                for j in missing:
                    board = originboard
                    board[i[0]][i[1]] = j
                    if type=="row":
                        if isValidArray(getline(board,i[1],False)) and isValidArray(getsubboard(board,getboardindex(i[0],i[1]))):  #column valid
                            if calculate(board,result):
                                return True
                    elif type=="column":
                        if isValidArray(getline(board,i[0],True)) and isValidArray(getsubboard(board,getboardindex(i[0],i[1]))):  #column valid
                            if calculate(board,result):
                                return True
                    else:
                        if isValidArray(getline(board,i[0],True)) and isValidArray(getline(board,i[1],False)):  #column valid
                            if calculate(board,result):
                                return True

            return False

        result = []
        calculate(board,result)
        if len(result)>0:
            return result[0]
        return None
if __name__=="__main__":
    s = Solution()
    sudoku_source = 	["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]

    sudoku = [list(i) for i in sudoku_source]
    for i in sudoku:
        for j in xrange(len(i)):
            if i[j]!=".":
                i[j] = int(i[j])
    print s.solveSudoku(sudoku)




