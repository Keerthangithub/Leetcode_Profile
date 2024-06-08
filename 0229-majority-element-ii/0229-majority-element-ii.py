class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        s=[]
        k=set()
        if len(nums)==1:
            return nums
        if len(nums)==2:
            for i in range(len(nums)):
                if nums[i]==nums[i+1]:
                    s.append(nums[i])
                    return s
                else:
                    return nums
        else:
            for i in nums:
                if nums.count(i)>len(nums)//3:
                    k.add(i)
            return k
        