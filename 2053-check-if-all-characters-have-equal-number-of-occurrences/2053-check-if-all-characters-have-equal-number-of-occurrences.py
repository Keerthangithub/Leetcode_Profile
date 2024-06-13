class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d={}
        c=s.count(s[0])
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i,j in d.items():
            if c==j:
                c=j
            else:
                return False
        return True