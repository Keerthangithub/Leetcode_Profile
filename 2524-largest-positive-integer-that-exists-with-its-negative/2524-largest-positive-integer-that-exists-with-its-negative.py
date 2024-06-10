class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            if -i in nums and i>=c:
                c=i
        if c==0:
            return -1
        return c