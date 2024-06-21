class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        d=list(s.split(" "))
        v=""
        for i in range(len(d)):
            if i<k-1:
                v+=d[i]
            if i==k-1:
                v+=d[i]
                break
            v+=" "
        return v