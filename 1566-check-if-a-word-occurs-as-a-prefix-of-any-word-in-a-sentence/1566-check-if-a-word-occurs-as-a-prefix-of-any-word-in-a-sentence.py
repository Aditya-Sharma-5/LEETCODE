class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        # a = -1
        ans = sentence.split()
        l = len(searchWord)
        for i in ans:
            if searchWord in i:
                if searchWord == i[:l]:
                    return (ans.index(i) + 1)
        return -1
        