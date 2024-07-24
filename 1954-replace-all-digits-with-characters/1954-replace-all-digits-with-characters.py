class Solution:
    def replaceDigits(self, s: str) -> str:
        d=""
        for i in range(len(s)):
            if i%2==0:
                d+=s[i]
            else:
                d+=chr(ord(s[i-1])+int(s[i]))
        return d