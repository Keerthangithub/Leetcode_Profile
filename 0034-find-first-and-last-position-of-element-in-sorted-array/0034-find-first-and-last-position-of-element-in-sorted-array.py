class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s=[]
        l=[]
        if len(nums)==0:
            return [-1,-1]
        for i in range(len(nums)):
            if nums[i]==target:
                s.append(i)
        if s==[]:
            return [-1,-1]
        if len(s)==1:
            s.append(s[0])
            return s
        if len(s)>=3:
            return s[0],s[len(s)-1]
        return s