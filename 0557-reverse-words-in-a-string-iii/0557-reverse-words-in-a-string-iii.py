class Solution:
    def reverseWords(self, s: str) -> str:
        ans = s.split()
        res = []

        for i in ans:
            a = i[::-1]
            res.append(a)
        x = " ".join(res)
        # print(res)
        return x
        