class Solution:
    def findLucky(self, arr: List[int]) -> int:
        k=0
        d={}
        arr.sort()
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in d:
            if i==d[i]:
                k=i
        if k==0:
            return -1
        return k