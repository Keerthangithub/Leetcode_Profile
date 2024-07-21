class Solution:
    def reverseWords(self, s: str) -> str:
        d=""
        v=s.split(" ")
        for i in range(len(v)):
            d+=v[i][::-1]
            if i!=len(v)-1:
                d+=" "
        return d