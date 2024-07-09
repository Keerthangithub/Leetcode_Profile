import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        def sqrt(number):
            x = number
            y = 0.5 * (x + number / x)
            while x != y:
                x = y
                y = 0.5 * (x + number / x)
            return math.floor(x)
        s,g,d=0,0,0
        while(1):
            if s==k:
                break
            s+=1
            g=gifts.index(max(gifts))
            d=sqrt(max(gifts))
            gifts[g]=d
        return sum(gifts)