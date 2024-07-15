class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        c=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j]<=prices[i]:
                    prices[i]=abs(prices[j]-prices[i])
                    break
        return prices
            