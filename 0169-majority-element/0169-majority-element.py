class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i,j in d.items():
            if j>len(nums)//2:
                return i
        '''for i in nums:
            if nums.count(i)>len(nums)//2:
                return i'''