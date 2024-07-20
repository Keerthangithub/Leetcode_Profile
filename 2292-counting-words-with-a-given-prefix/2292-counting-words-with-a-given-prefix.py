class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        d=""
        c=0
        for i in words:
            if len(i)>=len(pref):
                for j in range(len(pref)):
                    d+=i[j]
                if d==pref:
                    c+=1
                d=""
            else:
                continue
        return c

