class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        res = s.split(" ")
        if len(pattern)!= len(res):
            return False
        
        if len(set(pattern)) != len(set(res)):
            return False
        dict1 = {}

        for i in range(len(pattern)) :
            if res[i] not in dict1:
                dict1[res[i]] = pattern[i]
            elif dict1[res[i]] != pattern[i]:
                return False
        return True

            # else:
            #     dict1[pattern[i]] = res[i]
        
        # for i in range(len(pattern)):
        #     if dict1[pattern[i]] != res[i]:
        #         return False
        #     return True

        # for i in range(len(words)):
        #     if words[i] not in w_to_p: 
        #         w_to_p[words[i]] = p[i]
        #     elif w_to_p[words[i]] != p[i]: 
        #         return False

        # return True