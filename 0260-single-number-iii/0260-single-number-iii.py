class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d={}
        k=[]
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i,j in d.items():
            if j==1:
                k.append(i)
        return k