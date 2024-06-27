class Solution:
    def countElements(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            if i!=min(nums) and i!=max(nums):
                c+=1
        return c