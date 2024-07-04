class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        k=len(s)//2
        c,d=0,0
        for i in range(k):
            j=i+k
            if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' or s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U':
                c+=1
            if s[j]=='a' or s[j]=='e' or s[j]=='i' or s[j]=='o' or s[j]=='u' or s[j]=='A' or s[j]=='E' or s[j]=='I' or s[j]=='O' or s[j]=='U':
                d+=1
        if c==d:
            return True
        return False