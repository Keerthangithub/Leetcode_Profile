class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        c,d=0,0
        for i in nums:
            if i<0:
                c+=1
            else:
                if i!=0:
                    d+=1
        if c>d:
            return c
        return d