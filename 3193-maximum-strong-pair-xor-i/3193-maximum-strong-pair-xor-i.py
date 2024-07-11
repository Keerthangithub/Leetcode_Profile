class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        k=0
        for i in nums:
            for j in nums:
                if abs(i-j)<=min(i,j):
                    if k<(i^j):
                        k=i^j
        return k