class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s,k=0,1
        for i in str(n):
            s+=int(i)
            k=k*int(i)
        return k-s