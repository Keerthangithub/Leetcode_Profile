class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        d=max(nums)
        s=0
        for i in range(k):
            s=s+d
            d=d+1
        return s
