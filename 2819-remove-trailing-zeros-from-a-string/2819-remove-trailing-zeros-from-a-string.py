class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        num = num[::-1]
        cnt = 0
        for i in num:
            if i == '0':
                cnt += 1
            else:
                break
        new = num[cnt:]
        return new[::-1]

        