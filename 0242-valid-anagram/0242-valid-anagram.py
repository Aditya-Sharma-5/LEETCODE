class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a = ''.join(sorted(s))
        b = ''.join(sorted(t))
        print(a)
        print("hello :", b)
        if a == b:
            return True
        return False