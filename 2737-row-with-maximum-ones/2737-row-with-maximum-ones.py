class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        row = -1
        maxi = 0
        for i in range(len(mat)):
            maxm = mat[i].count(1)
            if maxi < maxm:
                maxi = maxm
                row = i
        if maxi == 0:
            return [0 , 0]
        else:
            return [row , maxi]
        