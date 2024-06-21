class Solution:
    def arraySign(self, nums: List[int]) -> int:
        s=1
        for i in range(len(nums)):
            s=s*nums[i]
        if s<0:
            return -1
        if s>0:
            return 1
        return 0