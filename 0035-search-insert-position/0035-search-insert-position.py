class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        g=len(nums)-1
        for i in range(len(nums)):
            if nums[i]==target:
                return i
            else:
                c=1
        if c==1:
            for i in range(len(nums)):
                if target==nums[i]+1:
                    return i+1
                if target==nums[i]-1:
                    return i
                if target<nums[0]:
                    return 0
                if target>nums[g]:
                    if(i==len(nums)-1):
                        return len(nums)