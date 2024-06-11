class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        d=list(s.split(" "))
        s={}
        for i in d:
            if i not in s:
                s[i]=len(i)
        for i,j in s.items():
            if i!="":
                c=j
        return c