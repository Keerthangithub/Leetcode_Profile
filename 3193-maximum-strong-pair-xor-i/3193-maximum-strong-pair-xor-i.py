class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        d=0
        k=0
        for i in nums:
            for j in nums:
                if abs(i-j)<=min(i,j):
                    d=i^j
                    if k<d:
                        k=d
        return k