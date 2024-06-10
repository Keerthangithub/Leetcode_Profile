class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        c=0
        k=set()
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i,j in d.items():
            k.add(j)
            c+=1
        if c==len(k):
            return True
        return False