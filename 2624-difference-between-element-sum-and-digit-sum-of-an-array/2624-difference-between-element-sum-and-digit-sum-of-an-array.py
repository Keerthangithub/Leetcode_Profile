class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s=0
        k=[]
        for i in nums:
            k.append(str(i))
        for i in k:
            for j in i:
                s+=int(j)
        return abs(s-sum(nums))