class Solution:
    def countPrimes(self, n: int) -> int:
        if (n == 0) or n==1:
            return 0
        count = 0
        prime = []
        for i in range(n+1):
            prime.append("True")
        prime[0] = False
        prime[1] = False
        for i in range(2 , n):
            if prime[i]:
                count +=1
                j = 2*i
                while(j<n):
                    prime[j] = 0
                    j = j +i
        return count