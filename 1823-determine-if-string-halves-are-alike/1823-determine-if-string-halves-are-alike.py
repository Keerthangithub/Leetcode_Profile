class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        c,d=0,0
        for i in range(len(s)//2):
            if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' or s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U':
                c+=1
            if s[i+(len(s)//2)]=='a' or s[i+(len(s)//2)]=='e' or s[i+(len(s)//2)]=='i' or s[i+(len(s)//2)]=='o' or s[i+(len(s)//2)]=='u' or s[i+(len(s)//2)]=='A' or s[i+(len(s)//2)]=='E' or s[i+(len(s)//2)]=='I' or s[i+(len(s)//2)]=='O' or s[i+(len(s)//2)]=='U':
                d+=1
        if c==d:
            return True
        return False