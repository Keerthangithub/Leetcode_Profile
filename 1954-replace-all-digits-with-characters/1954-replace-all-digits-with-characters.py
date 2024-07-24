class Solution:
    def replaceDigits(self, s: str) -> str:
        d=""
        for i in range(len(s)):
            if i%2==0:
                d+=s[i]
            else:
                k=ord(s[i-1])+int(s[i])
                d+=chr(k)
        return d