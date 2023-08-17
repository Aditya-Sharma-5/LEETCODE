class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict1 = {"2": "abc" , "3":"def" , "4":"ghi" , "5":"jkl" , "6":"mno" , "7":"pqrs" , "8":"tuv" , "9":"wxyz"}
        ans = []
        if(len(digits) ==0):
            return ans

        def solve(digits , ans , index , temp):

            if index == len(digits):
                ans.append(temp)
                return

            # val = dict1[digits[index]]
            for i in dict1[digits[index]]:
                # temp += i
                solve(digits , ans  , index+1 , temp+i)

        
        solve(digits , ans  , 0 , "")
        return ans