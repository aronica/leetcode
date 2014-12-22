class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        def __getindex__(n,index):
            return (index/n,index%n)
            
        if matrix is None or target is None or len(matrix) == 0 or len(matrix[0])==0:
            return False
        m = len(matrix)
        n = len(matrix[0])
        low ,high = 0,m*n-1
        while low<=high:
            mid = low + ((high-low)>>1)
            index = __getindex__(n,mid)
            if matrix[index[0]][index[1]] == target:
                return True
            elif matrix[index[0]][index[1]]<target:
                low = mid + 1
            else:
                high = mid - 1
        return False
                
        