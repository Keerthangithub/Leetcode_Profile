class Solution:
    def scoreOfString(self, s: str) -> int:
        d=0
        for i in range(len(s)-1):
            d+=abs(ord(s[i])-ord(s[i+1]))
        return d