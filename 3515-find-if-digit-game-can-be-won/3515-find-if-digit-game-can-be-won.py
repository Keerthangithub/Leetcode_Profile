class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        s,x=0,0
        for i in nums:
            if i>=0 and i<=9:
                s+=i
            else:
                x+=i
        if s==x:
            return False
        return True