class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        k=[]
        c=0
        for i in range(len(nums)):
            c+=nums[i]
            k.append(c)
        return k