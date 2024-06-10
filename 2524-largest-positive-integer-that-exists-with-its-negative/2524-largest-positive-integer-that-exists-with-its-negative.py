class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        k=[]
        for i in nums:
            if -i in nums:
                k.append(i)
                k.append(-i)
        if k==[]:
            return -1
        return max(k)