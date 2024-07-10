class Solution:
    def minOperations(self, logs: List[str]) -> int:
        c=0
        for i in logs:
            if i!='../' and i!='./':
                c+=1
            if i=='../':
                c-=1
            if c<0:
                c=0
        if c<=0:
            return 0
        return c