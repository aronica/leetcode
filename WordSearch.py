__author__ = 'fafu'
class Solution:
    def exist(self, board, word):
        if board is None or len(board)<1 or word is None or len(word)==0:
            return False
        i = 0
        m = 0
        #direction:up 1, right 2,down 3, left 4
        li = dict({i:-1 for i in xrange(len(board))})
        while i<len(board):
            index = board[i][li[i]+1:].find(word[m])
            if index == -1:
                i += 1
            else:
                li[i] = index
                stack = list()
                pre = None
                line = i
                while len(stack)>0 or line is not None:
                    if line is not None:
                        if line != 0:
                            if pre is None or pre=='up':
                                if board[i-1][index] == word[m+1]:
                                    stack.append((i,index,1,m)) # row,index,direction
                                    line = i - 1
                                    pre = 'up'
                                    continue
                            elif i!= len(board[i]-1) and board[i][index+1] == word[m+1]:
                                stack.append((i,index,2,m)) # row,index,direction









