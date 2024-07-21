class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c,k=0,0
        for i in words:
            d=""
            d=i
            c=0
            for j in d:
                if j in allowed:
                    c+=1
                else:
                    break
            if c==len(d):
                k+=1
        return k
            