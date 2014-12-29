class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if len(matrix)==0 or len(matrix[0])==0:
            return 0
        row = len(matrix)
        column = len(matrix[0])
        i,j = 0,0
        maxarea = 0
        while i<row:
            j = 0
            while j<column:
                if i == 0:
                    if j == 0:
                        matrix[0][0] = matrix[0][0] == "1" and "0,0" or None
                    else:
                        matrix[i][j] = matrix[i][j]!="0" and (matrix[i][j-1] is None and str(i)+","+str(j) or matrix[i][j-1]) or None
                else:
                    if j == 0:
                        matrix[i][j] = matrix[i][j] != "0" and (matrix[i-1][j] is None and str(i)+","+str(j) or matrix[i-1][j]) or None
                    else:
                        if matrix[i][j] == "0":
                            matrix[i][j] = None
                        else:
                            if matrix[i][j-1] is None and matrix[i-1][j] is None:
                                matrix[i][j] = str(i)+","+str(j)
                            elif matrix[i][j-1] is not None and matrix[i-1][j] is None:
                                arr = matrix[i][j-1].split(":")
                                arr = min([int(a.split(",")[1]) for a in arr])
                                matrix[i][j] = str(i)+","+str(arr)
                            elif matrix[i][j-1] is None and matrix[i-1][j] is not None:
                                arr = matrix[i-1][j].split(":")
                                arr = min([int(a.split(",")[0]) for a in arr])
                                matrix[i][j] = str(arr)+","+str(j)
                            else:
                                left ,top= matrix[i][j-1],matrix[i-1][j]
                                left_array = left.split(":")
                                top_array = top.split(":")
                                left_array = [(int(a.split(",")[0]),int(a.split(",")[1])) for a in left_array]
                                top_array = [(int(a.split(",")[0]),int(a.split(",")[1])) for a in top_array]
                                res = set()
                                for a,b in left_array:
                                    found = False
                                    minx = j
                                    for x,y in top_array:
                                        if a>=x:
                                            found = True
                                            res.add((a,b))
                                            break
                                        else:
                                            if minx>x:
                                                minx = x
                                    if not found:
                                        res.add((minx,b))

                                for a,b in top_array:
                                    found = False
                                    miny = x
                                    for x,y in left_array:
                                        if b>=y:
                                            found = True
                                            res.add((a,b))
                                            break
                                        else:
                                            if miny>y:
                                                miny = y
                                    if not found:
                                        res.add((a,miny))
                                matrix[i][j] = ":".join([str(a[0])+","+str(a[1]) for a in res])
                if matrix[i][j] is not None:
                    try:
                        arr = [(int(a.split(",")[0]),int(a.split(",")[1])) for a in matrix[i][j].split(":")]
                        maxarea = max(max([(i-a[0]+1)*(j-a[1]+1) for a in arr]),maxarea)
                    except KeyError as e:
                        raise

                j += 1
            i+=1
        return maxarea
if __name__=="__main__":
    s = Solution()
    a = [["1","0","0","1","1"],
         ["0","0","1","1","0"],
         ["1","1","1","1","1"],
         ["0","1","1","0","1"]
    ]
   # print s.maximalRectangle(a)
    a=["1011100010","0100000110","0101000011","1110000010","0111001010","1101101110"]
    a= [[i for i in j] for j in a]
    print a

    print s.maximalRectangle(a)











