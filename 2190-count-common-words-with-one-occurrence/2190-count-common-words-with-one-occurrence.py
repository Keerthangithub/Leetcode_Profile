class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        d={}
        c=0
        k=list(set(words1))
        v=list(set(words2))
        k.extend(v)
        for i in k:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            if d[i]==2 and words1.count(i)==1 and words2.count(i)==1:
                c+=1
        return c
