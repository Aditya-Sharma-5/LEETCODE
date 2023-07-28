class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            a = target-nums[i]
            if a in nums:
                j = nums.index(a)
                if j == i:
                    continue
                break
        return i , j