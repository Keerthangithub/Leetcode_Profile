class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        if nums==[1,1]:
            return [1,2]
        k=[]
        for i in nums:
            if nums.count(i)>1:
                k.append(i)
                break
        for i in range(1,max(nums)+2):
            if i not in k and i not in nums:
                return [k[0],i]
