class Solution:
    def digitCount(self, num: str) -> bool:
        s=""
        for i in range(len(num)):
            s+=num[i]
            if (num.count(str(i))==int(s)):
                c=0
                s=""
            else:
                return False
        if c==0:
            return True