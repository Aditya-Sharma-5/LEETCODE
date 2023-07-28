class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:   
        # print(points)     
        points.sort(key=lambda x:x[1])
        # print(points)

        res, curEnd = 1, points[0][1]
        # print(curEnd)

        for start,end in points:
            # print(start)

            if start>curEnd:

                curEnd = end

                res += 1

        return res