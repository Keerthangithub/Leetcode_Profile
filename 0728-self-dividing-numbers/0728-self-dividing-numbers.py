class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        k=[]
        c=0
        for i in range(left,right+1):
            d=""
            if i<10:
                k.append(i)
            if i>10:
                d=str(i)
                for j in d:
                    if j!='0' and i%int(j)==0:
                        c+=1
                if c==len(d):
                    k.append(i)
            c=0
        return k
                 