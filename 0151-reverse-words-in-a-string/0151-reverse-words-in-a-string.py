class Solution:
    def reverseWords(self, s: str) -> str:
        k=s.split(" ")
        k=list(filter(lambda x: x != '', k))
        #return k
        d=""
        for i in range(len(k)-1,-1,-1):
            if i!=0:
                d+=k[i]
                d+=" "
            else:
                d+=k[i]
                break
        return d
