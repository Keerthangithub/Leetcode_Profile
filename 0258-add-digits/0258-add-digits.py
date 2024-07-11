class Solution:
    def addDigits(self, num: int) -> int:
        s=0
        while(1):
            for i in str(num):
                s+=int(i)
            if len(str(s))>1:
                num=str(s)
                s=0
            else:
                return s
