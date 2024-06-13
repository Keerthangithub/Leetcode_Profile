class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        c=0
        k=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j]<nums[i]:
                    c+=1
            k.append(c)
            c=0
        return k