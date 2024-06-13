class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        c=0
        k=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j]<nums[i]:
                    c+=1
            k.append(c)
            c=0
        return k

        '''d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i,j in d.items():
            for x,y in d.items():
                if x<i:
                    c+=y
            k.append(c)
            c=0
        return k'''