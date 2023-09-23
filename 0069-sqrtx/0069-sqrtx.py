import math
class Solution:
    def mySqrt(self, num: int) -> int:
        # return int(math.sqrt(x))
        s = 0 
        e = num
        ans = -1
        while(s<=e):
            mid = s + (e-s)//2
            if (mid*mid) == num:
                return mid
            elif (mid*mid) < num:
                ans = mid
                s = mid+1
            else:
                e = mid-1
        return ans