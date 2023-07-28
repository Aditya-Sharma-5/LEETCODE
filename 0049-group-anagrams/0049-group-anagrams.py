class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for i in strs:
            sorted_word="".join(sorted(i))
            if sorted_word not in dic:
                dic[sorted_word]=[i]
            else:
                dic[sorted_word].append(i)
        return dic.values()
