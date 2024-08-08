class Solution:
    def generateTheString(self, n: int) -> str:
        d=""
        if n%2==0:
            for i in range(n):
                if i==n-1:
                    d+='b'
                else:
                    d+='a'
        else:
            for i in range(n):
                d+='a'
        return d