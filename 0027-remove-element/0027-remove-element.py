class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c,d=0,0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[c]=nums[i]
                c+=1
            else:
                d+=1
        return len(nums)-d