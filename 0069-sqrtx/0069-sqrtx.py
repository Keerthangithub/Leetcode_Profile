class Solution:
    def mySqrt(self, x: int) -> int:
        k=[]
        c=0
        y=x**0.5
        k.append(str(y))
        for i in k:
            if i==".":
                c=1
                break
            else:
                c=0
        if c==1:
            return k[0]
        else:
            return int(y)
