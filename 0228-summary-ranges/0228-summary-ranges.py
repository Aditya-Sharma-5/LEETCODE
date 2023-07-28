class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums :
            return []

        ans = []
        start = end = nums[0]

        for i in range(1 , len(nums)):
            if nums[i] == end +1:
                end = nums[i]
            else:
                if start != end :
                    ans.append(f"{start}->{end}")
                else:
                    ans.append(str(start))

                start = end = nums[i]
        if start != end :
            ans.append(f"{start}->{end}")
        else:
            ans.append(str(start))
        
        return ans

