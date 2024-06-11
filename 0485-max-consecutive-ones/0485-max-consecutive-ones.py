class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        k=[]
        for i in nums:
            if i==1:
                c+=1
            else:
                k.append(c)
                c=0
        k.append(c)
        return max(k)