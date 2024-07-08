class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        k=[]
        for i in range(1,n+1):
            k.append(i)
        i,s=0,0
        while(1):
            if i==n-1:
                i=0
                k.reverse()
            if s==time:
                return k[i]
            i+=1
            s+=1