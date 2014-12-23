__author__ = 'fafu'
class Solution:
    #Solution:
    # First step: Find all the points with value of 'O' on the 4 edges of the rectangle
    # Second step: Find out all the inner points with value 'O' that is adjacent with the points we found,add it to an set,
    #     these points are the points that is not surrounded by "X"
    #Third step: Change all the inner points with value "O" that is in the set we found in step 2

    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if board is None or len(board)<3:
            return
        lens = len(board)
        lencolumn = len(board[0])
        result = set()
        tmp = []
        li = [(0,None),(None,0),(None,lencolumn-1),(lens-1,None)]
        for k,v in li:
            if v is None:
                i = 1
                another = k == 0 and 1 or lens-2
                while i<lencolumn-1:
                    if board[k][i] == "O":
                        if board[another][i] == "O":
                            tmp.append((another,i))
                            result.add((another,i))
                    i += 1
            else:  #k is None
                i = 1
                another = v == 0 and 1 or lencolumn-2
                while i<lens-1:
                    if board[i][v] == "O":
                        if board[i][another]=="O":
                            tmp.append((i,another))
                            result.add((i,another))
                    i += 1
        while len(tmp)>0:
            i,j = tmp.pop(0)
            if i != 1:
                if board[i-1][j] == "O" and (i-1,j) not in result:
                    result.add((i-1,j))
                    tmp.append((i-1,j))
            if i != lens-1:
                if board[i+1][j] == "O" and (i+1,j) not in result:
                    result.add((i+1,j))
                    tmp.append((i+1,j))
            if j != 1:
                if board[i][j-1] == "O" and (i,j-1) not in result:
                    result.add((i,j-1))
                    tmp.append((i,j-1))
            if j != lencolumn-1:
                if board[i][j+1] == "O" and (i,j+1) not in result:
                    result.add((i,j+1))
                    tmp.append((i,j+1))
        i ,j = 1, 1
        while i<lens-1:
            j = 1
            tmp = [board[i][0]]
            while j<lencolumn-1:
                if board[i][j]=="O" and (i,j) not in result or board[i][j]=="X":
                    tmp.append("X")
                else:
                    tmp.append("O")
                j += 1
            tmp.append(board[i][lencolumn-1])
            board[i] = "".join(tmp)
            i += 1
if __name__=="__main__":
    s = Solution()
    board = ["XOXX",
             "OXOX",
             "XOXO",
             "OXOX",
             "XOXO",
             "OXOX"]
    s.solve(board)
    print board




















