class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i,j in d.items():
            c=j
            break
        for i,j in d.items():
            if c==j:
                c=j
            else:
                return False
        return True
        '''k=[]
        d=set(s)
        for i in d:
            for j in s:
                if i==j:
                    c+=1
            k.append(c)
        for i in range(len(k)-1):
            if k[i]!=k[i+1]:
                return False
        return True'''