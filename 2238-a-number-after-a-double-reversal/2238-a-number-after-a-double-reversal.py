class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        k=str(num)
        if num==0:
            return True
        elif k[-1]=='0':
            return False
        else:
            return True