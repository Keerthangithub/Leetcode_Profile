class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        c=""
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i,j in d.items():
            if j==1:
                c+=i
                break
        if c=="":
            return -1
        return s.index(c)