class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d={}
        k=[]
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i,j in d.items():
            if j==2:
                k.append(i)
        return k