class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=[]
        for i in range(len(nums)):
            if nums[i]!=0:
                k.append(nums[i])
        for i in range(len(nums)):
            if nums[i]==0:
                k.append(nums[i])
        for i in range(len(nums)):
            nums[i]=k[i]
        return nums