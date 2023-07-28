class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map1 = {}
        for i in magazine:
            if i in map1:
                map1[i] += 1
            else:
                map1[i] = 1
        print(map1)
        for i in range(len(ransomNote)):
            if ransomNote[i] in map1:
                if map1[ransomNote[i]] >=1:
                    map1[ransomNote[i]] -= 1
                elif map1[ransomNote[i]] == 0:
                    return False
            if ransomNote[i] not in map1:
                return False


        return True