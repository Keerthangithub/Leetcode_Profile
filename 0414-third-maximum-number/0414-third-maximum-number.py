class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        s=list(set(nums))
        s.sort()
        if len(s)<=2:
            return max(s)
        return s[-3]
