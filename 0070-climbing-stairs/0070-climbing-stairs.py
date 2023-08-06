class Solution:
    def climbStairs(self, n: int) -> int:
        def giveAns(n , dp): 
            if n == 0:
                return 1
            if n<0:
                return 0
            if dp[n]!= -1:
                return dp[n]

            x = giveAns(n-1 , dp) + giveAns(n-2 , dp)
            dp[n] = x
            return giveAns(n-1 , dp) + giveAns(n-2 , dp)

        dp = [-1 for i in range(n+1)]
        a = giveAns(n , dp)
        return a