class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c=0
        d=[]
        v=[]
        for i in nums:
            v.append(str(i))
        for i in v:
            c=0
            for j in i:
                c+=1
            d.append(c)
        c=0
        for i in d:
            if i%2==0:
                c+=1
        return c
            