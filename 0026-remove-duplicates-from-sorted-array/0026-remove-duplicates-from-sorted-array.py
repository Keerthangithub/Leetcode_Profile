class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums.sort()
        c=0
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        #nums=['_']*len(nums)
        for i in d:
            nums[c]=i
            c+=1
        return c