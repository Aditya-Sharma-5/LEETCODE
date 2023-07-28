class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # dict1 = {}
        # dict2 = {}
        # for i in s:
        #     if i not in dict1:
        #         dict1[i] = 1
        #     else:
        #         dict1[i] +=1
        # for i in t:
        #     if i not in dict2:
        #         dict2[i] = 1
        #     else:
        #         dict2[i] +=1
        # print(dict1 )
        # print(dict2)
        # print(len(dict1))
        # print(len(dict2))
        # if len(dict1) != len(dict2):
        #     return False

        # return True

        map1 = []
        map2 = []
        for i in s:
            map1.append(s.index(i))  # storing the index of string s
        for i in t:
            map2.append(t.index(i))   # storing the index of string t

# comparing the index values of both maps
        if map1 == map2:
            return True
        return False



