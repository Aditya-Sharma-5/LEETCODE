class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def solve(nums,ans,temp,index):
            
            if(index >= len(nums)):
                ans.append(temp.copy())
                return
            
            # lunga
            temp.append(nums[index])
            solve(nums,ans, temp ,index+1)
            temp.pop()
            
            # nhilunga
            solve(nums,ans, temp,index+1)
            
        solve(nums,ans,[],0)
        
        return ans