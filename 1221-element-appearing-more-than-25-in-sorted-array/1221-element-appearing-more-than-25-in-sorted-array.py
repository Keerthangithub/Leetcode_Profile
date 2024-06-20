class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        k=[]
        d={}
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i,j in d.items():
            k.append(j)
        for i in d:
            if d[i]==max(k):
                return i