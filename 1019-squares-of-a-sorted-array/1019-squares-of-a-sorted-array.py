class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        k=[]
        for i in nums:
            k.append(i*i)
        k.sort()
        return k