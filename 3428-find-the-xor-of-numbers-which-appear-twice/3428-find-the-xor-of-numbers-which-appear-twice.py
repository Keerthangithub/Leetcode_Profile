class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        s=[]
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i,j in d.items():
            if j>1:
                s.append(i)
        if s==[]:
            return 0
        if len(s)==1:
            return s[0]
        k=s[0]
        for i in range(1,len(s)):
            k=k^s[i]
        return k