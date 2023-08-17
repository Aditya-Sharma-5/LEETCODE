class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 or nums.count(target) == 0:
            return [-1 , -1]

        ans = []
        index = 0
        for i in range(len(nums)):
            if nums[i] == target:
                ans.append(i)

        return [ans[0] , ans[-1]]

