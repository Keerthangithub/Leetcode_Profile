class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        d,s=0,0
        for i in accounts:
            s=0
            for j in range(len(i)):
                s+=i[j]
            if d<s:
                d=s
        return d