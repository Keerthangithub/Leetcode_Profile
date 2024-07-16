class Solution:
    def pivotInteger(self, n: int) -> int:
        k,s=0,0
        for i in range(1,n+1):
            k+=i
            s=0
            for j in range(i,n+1):
                s+=j
            if k==s:
                return i
        return -1
