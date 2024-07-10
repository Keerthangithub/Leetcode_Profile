class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        d={}
        v=[]
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if nums[i][j] in d:
                    d[nums[i][j]]+=1
                else:
                    d[nums[i][j]]=1
        for i,j in d.items():
            if j==len(nums):
                v.append(i)
        if v==[]:
            return []
        v.sort()
        return v