class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        dict1 = {}
        # create intial dicitionar
        for i in nums:
            dict1[i] = True
            
        def solve(ans,nums,dict1,temp):
            
            if(len(temp) == len(nums)):
                ans.append(temp.copy())
                return
            
            for key in dict1.keys():
                if(dict1[key] == True):
                    temp.append(key)
                    dict1[key] = False
                    solve(ans,nums,dict1,temp)
                    dict1[key] = True
                    temp.pop()
            
        
        solve(ans,nums,dict1,[])
        return ans