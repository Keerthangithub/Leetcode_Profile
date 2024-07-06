class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        s=[]
        k=[]
        for i in range(1,n):
            for j in range(i+1,n+1):
                if(i/j not in k):
                    k.append(i/j)
                    s.append(str(i)+"/"+str(j))
        return s