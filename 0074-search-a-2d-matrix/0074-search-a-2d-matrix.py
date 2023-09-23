class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # row = len(matrix)
        # col = len(matrix[0])
        # n = col*row
        # s = 0 
        # e = n-1
        # mid = s +(e-s)//2
        # while s<=e:
        #     rowIndex = mid//col
        #     colIndex = mid%col
        #     currNumber = matrix[rowIndex][colIndex]
        #     if currNumber == target:
        #         return True
        #     elif (target >currNumber):
        #         s = mid +1
        #     else:
        #         e = mid -1
        #     mid = s + (e - s)//2
        # return False
        for i in matrix:
            if target in i:
                return True
        return False