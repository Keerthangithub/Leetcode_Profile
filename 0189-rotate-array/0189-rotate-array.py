class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s=[0]*len(nums)
        i=0
        while i<len(nums):
            if (i+k)>=len(nums):
                s[(i+k)%len(nums)]=nums[i]
            else:
                s[i+k]=nums[i] 
            i+=1
        for i in range(len(s)):
            nums[i]=s[i]
        return nums
        