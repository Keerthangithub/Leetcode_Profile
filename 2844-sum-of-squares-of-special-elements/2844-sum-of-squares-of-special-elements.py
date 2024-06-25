class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        k=[]
        c=0
        for i in range(1,len(nums)+1):
            if len(nums)%i==0:
                k.append(i)        
        for i in k:
            c=c+(nums[i-1]*nums[i-1])
        return c
